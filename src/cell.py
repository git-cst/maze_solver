from graphics import Window, Point, Line
from constants import ACCEPTED_FILL_COLOURS

class Cell():
    def __init__(self, window: Window = None):
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
        if self.__win == None:
            return 
        
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
        if self.__win == None:
            return 
        
        fill_colour = "red" if undo is False else "grey"

        center_position_x = self.__x2 - (self.__x2 - self.__x1) / 2
        center_position_y = self.__y2 - (self.__y2 - self.__y1) / 2
        to_cell_center_position_x = to_cell.__x2 - (to_cell.__x2 - to_cell.__x1) / 2
        to_cell_center_position_y = to_cell.__y2 - (to_cell.__y2 - to_cell.__y1) / 2

        self.__win.draw_line(Line(Point(center_position_x, center_position_y), Point(to_cell_center_position_x, to_cell_center_position_y)), fill_colour)
