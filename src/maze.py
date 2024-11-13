from cell import Cell
from graphics import Window
from constants import ACCEPTED_FILL_COLOURS, WINDOW_COLOUR
import time; import random

def time_execution(func: function):
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

        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
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

    def _break_walls_r(self, i: int = 0, j: int = 0):
        current_cell: Cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            directions_to_visit = []

            if i > 0 and not self._cells[i- 1][j].visited: # UP
                directions_to_visit.append(('up', i - 1, j))
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited: # DOWN
                directions_to_visit.append(('down', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited: # LEFT
                directions_to_visit.append(('left', i, j - 1)) 
            if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited: # RIGHT
                directions_to_visit.append(('right', i, j + 1))

            if not directions_to_visit:
                self._draw_cell(i, j)
                return
 
            direction, ni, nj = random.choice(directions_to_visit)

            next_cell: Cell = self._cells[ni][nj]
            if direction == 'up': # GO UP
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == 'down': # GO DOWN
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif direction == 'left': # GO LEFT
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == 'right': # GO RIGHT
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False

            i, j = ni, nj
            self._break_walls_r(i, j)
    
    @time_execution
    def solve_maze(self, func):
        algorithms = ["DFS", "BFS", "a_star"]

        if func in algorithms:
            return getattr(self, func)()
        else:
            return f"Unknown algorithm chosen. Implemented algorithms are {', '.join(algorithms)}"

    def DFS(self):
        time.sleep(1)

    def BFS(self):
        time.sleep(1)

    def a_star(self):
        time.sleep(1)

    def _reset_visited(self):
        for i in range(0, self.__num_rows):
            for j in range(0, self.__num_cols):
                self._cells[i][j].visited = False

    def _animate_self(self) -> None:
        self.__win.redraw()
        #time.sleep(0.5)