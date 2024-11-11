from cell import Cell
from graphics import Window
from constants import ACCEPTED_FILL_COLOURS
import time

class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, line_colour: str = None, win: Window = None):
        if line_colour not in ACCEPTED_FILL_COLOURS and line_colour != None:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")

        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
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
        
        cell = self._cells[i][j]

        x_movement = j * self.__cell_size_x
        y_movement = i * self.__cell_size_y

        x1 = self.__x1 + x_movement
        y1 = self.__y1 + y_movement
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell.draw(x1, y1, x2, y2, self.__line_colour)
        
        self._animate_self()

    def _animate_self(self) -> None:
        self.__win.redraw()
        time.sleep(0.05)