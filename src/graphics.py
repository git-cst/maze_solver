from tkinter import Tk, BOTH, Canvas
from constants import ACCEPTED_FILL_COLOURS
import time

class Point():
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_colour: str) -> None:
        if fill_colour not in ACCEPTED_FILL_COLOURS:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")
        
        canvas.create_line(self.point1.__x, self.point1.__y, self.point2.__x, self.point2.__y, fill=fill_colour, width=2)

class Window():
    def __init__(self, width: int, height: int):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze solver")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas_widget = Canvas(master=self.__root_widget, bg="white", height=height, width=width)
        self.__canvas_widget.pack(fill=BOTH, expand=1)

        self.__running = False

    def redraw(self) -> None:
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line: Line, fill_colour: str):
        if fill_colour not in ACCEPTED_FILL_COLOURS:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")

        line.draw(self.__canvas_widget, fill_colour)

    def close(self) -> None:
        self.__running = False

class Cell():
    def __init__(self, window: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int, fill_colour: str) -> None:
        if fill_colour not in ACCEPTED_FILL_COLOURS:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")

        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2
        
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), fill_colour)
            
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), fill_colour)
            
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), fill_colour)
            
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), fill_colour)

    def draw_move(self, to_cell, undo: bool=False):
        fill_colour = "red" if undo is False else "grey"

        center_position_x = self.__x2 - (self.__x2 - self.__x1) / 2
        center_position_y = self.__y2 - (self.__y2 - self.__y1) / 2
        to_cell_center_position_x = to_cell.__x2 - (to_cell.__x2 - to_cell.__x1) / 2
        to_cell_center_position_y = to_cell.__y2 - (to_cell.__y2 - to_cell.__y1) / 2

        self.__win.draw_line(Line(Point(center_position_x, center_position_y), Point(to_cell_center_position_x, to_cell_center_position_y)), fill_colour)

class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

    def _create_cells(self):
        self.__cells = [[Cell(self.__win) for _ in range(self.__num_rows)] for _ in range(self.__num_cols)]

    def _draw_cell(self, i, j):
        pass

    def _animate_self(self):
        while self.__win.__running:
            self.__win.redraw()
            time.sleep(0.05)