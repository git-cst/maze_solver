from cell import Cell
from graphics import Window
from constants import ACCEPTED_FILL_COLOURS, WINDOW_COLOUR
import time; import random

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.4f} seconds to execute.")
        return result
    return wrapper

class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, line_colour: str = None, win: Window = None, seed = None):
        if line_colour not in ACCEPTED_FILL_COLOURS and line_colour != None:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")
        
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__seed = random.seed(seed) if seed != None else random.seed()
        self.__line_colour = line_colour if line_colour != None else "black"
        self.__win = win

    def _create_cells(self) -> None:
        self._cells = [[Cell(self.__win) for _ in range(self.__num_rows)] for _ in range(self.__num_cols)]

        for i in range(0, self.__num_cols):
            for j in range(0, self.__num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j) -> None:
        if self.__win == None:
            return 
        
        cell: Cell = self._cells[i][j]

        x_offset = j * self.__cell_size_x
        y_offset = i * self.__cell_size_y

        x1 = self.__x1 + x_offset
        y1 = self.__y1 + y_offset
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell.draw(x1, y1, x2, y2, self.__line_colour)
        
        self._animate_self()

    def _break_entrance_and_exit(self) -> None:
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        end_cell = self._cells[-1][-1]
        end_cell.has_bottom_wall = False

        if self.__win == None:
            return

        start_cell.draw(start_cell._x1, start_cell._y1, start_cell._x2, start_cell._y1, WINDOW_COLOUR)
        self._animate_self()
        end_cell.draw(end_cell._x1, end_cell._y2, end_cell._x2, end_cell._y2, WINDOW_COLOUR)
        self._animate_self()

    def _break_walls(self, start_i: int = 0, start_j: int = 0):
        stack = [(start_i, start_j)]
        while stack:
            i, j = stack[-1]
            current_cell = self._cells[i][j]
            if not current_cell.visited:
                current_cell.visited = True

            directions_to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:  # UP
                directions_to_visit.append(('up', i - 1, j))
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:  # DOWN
                directions_to_visit.append(('down', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:  # LEFT
                directions_to_visit.append(('left', i, j - 1))
            if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:  # RIGHT
                directions_to_visit.append(('right', i, j + 1))

            if directions_to_visit:
                direction, ni, nj = random.choice(directions_to_visit)
                next_cell = self._cells[ni][nj]
                if direction == 'up':
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                elif direction == 'down':
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
                elif direction == 'left':
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                elif direction == 'right':
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                stack.append((ni, nj))
            else:
                self._draw_cell(i, j)
                stack.pop()
                
    def _reset_visited(self):
        for i in range(0, self.__num_cols):
            for j in range(0, self.__num_rows):
                self._cells[i][j].visited = False
    
    @time_execution
    def solve(self, func, *args, **kwargs):
        algorithms = ["DFS", "BFS", "a_star"]

        if func in algorithms:
            return getattr(self, func)(*args, **kwargs)
        else:
            return f"Unknown algorithm chosen. Implemented algorithms are {', '.join(algorithms)}"

    def DFS(self, i: int = 0, j: int = 0, fill_colour = "red", offset: int = 0):
        self._animate_self()
        self._cells[i][j].visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        
        if i > 0 and not self._cells[i - 1][j].visited and self._cells[i][j].has_top_wall == False: # UP
            self._cells[i][j].draw_move(self._cells[i - 1][j], fill_colour=fill_colour, offset=offset)
            move_up = self.DFS(i - 1, j, fill_colour, offset)
            if move_up:
                return True
            else:
                self._cells[i - 1][j].draw_move(self._cells[i][j], True, fill_colour, offset)

        if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited and self._cells[i][j].has_bottom_wall == False: # DOWN
            self._cells[i][j].draw_move(self._cells[i + 1][j], fill_colour=fill_colour, offset=offset)
            move_down = self.DFS(i + 1, j, fill_colour, offset)
            if move_down:
                return True
            else:
                self._cells[i + 1][j].draw_move(self._cells[i][j], True, fill_colour, offset)

        if j > 0 and not self._cells[i][j - 1].visited and self._cells[i][j].has_left_wall == False: # LEFT
            self._cells[i][j].draw_move(self._cells[i][j - 1], fill_colour=fill_colour, offset=offset)
            move_left = self.DFS(i, j - 1, fill_colour, offset)
            if move_left:
                return True
            else:
                self._cells[i][j - 1].draw_move(self._cells[i][j], True, fill_colour, offset)

        if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited and self._cells[i][j].has_right_wall == False: # RIGHT
            self._cells[i][j].draw_move(self._cells[i][j + 1], fill_colour=fill_colour, offset=offset)
            move_right = self.DFS(i, j + 1, fill_colour, offset)
            if move_right:
                return True
            else:
                self._cells[i][j + 1].draw_move(self._cells[i][j], True, fill_colour, offset)
        
        return False
        
    def BFS(self, i: int = 0, j: int = 0, fill_colour = "red", offset: int = 0):
        ################### TO DO ######################
        # - IMPLEMENT IF IT THINKS IT'S BACKTRACKING?
        #   - HAVE TO TRACK IF IT IS BACKTRACKING TO AN ACTIVELY BEING EXPLORED PATH
        #   - WILL SLOW DOWN THE SOLUTION A BIT AS IT IS NOW WASTING TIME ON BACKTRACKING FOR "OUR" VISUAL ENJOYMENT...

        visited = []
        to_visit = []
        start_position = [self._cells[i][j], i, j, None]
        to_visit.append(start_position)

        unsolved = True
        while unsolved:
            self._animate_self()
            neighbouring_cells = []
            
            new_position: tuple[Cell, int, int, Cell]     = to_visit.pop(0)
            current_cell: Cell                            = new_position[0]
            current_column: int                           = new_position[1]
            current_row: int                              = new_position[2]
            parent_cell: Cell                             = new_position[3]

            if parent_cell:
                current_cell.visited = True
                parent_cell.draw_move(current_cell, fill_colour=fill_colour, offset=offset)

            visited.append(new_position)
            i, j = current_column, current_row

            if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
                unsolved = False
                continue

            if i > 0 and not self._cells[i - 1][j].visited and current_cell.has_top_wall == False: # UP
                neighbouring_cells.append([self._cells[i - 1][j], i - 1, j, current_cell])

            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited and current_cell.has_bottom_wall == False: # DOWN
                neighbouring_cells.append([self._cells[i + 1][j], i + 1, j, current_cell])

            if j > 0 and not self._cells[i][j - 1].visited and current_cell.has_left_wall == False: # LEFT
                neighbouring_cells.append([self._cells[i][j - 1], i, j - 1, current_cell])

            if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited and current_cell.has_right_wall == False: # RIGHT
                neighbouring_cells.append([self._cells[i][j + 1], i, j + 1, current_cell])        

            for cell in neighbouring_cells:
                if cell not in visited and cell not in to_visit:
                    to_visit.append(cell)

    def a_star(self):
        print("Solving using A*.")
        time.sleep(1)

    def _animate_self(self) -> None:
        self.__win.redraw()
        #time.sleep(0.5)