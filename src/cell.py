from graphics import Window, Point, Line
from constants import ACCEPTED_FILL_COLOURS, WINDOW_COLOUR, MAZE_LINE_WIDTH

class Cell():
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int, fill_colour: str) -> None:
        if self.__win == None:
            return 
        
        if fill_colour not in ACCEPTED_FILL_COLOURS:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")

        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2
        
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_colour)
        else:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), WINDOW_COLOUR)
            
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_colour)
        else:
            self.__win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), WINDOW_COLOUR)
            
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_colour)
        else:
            self.__win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), WINDOW_COLOUR)
            
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_colour)
        else:
            self.__win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), WINDOW_COLOUR)
            

    def draw_move(self, to_cell, undo: bool=False, fill_colour = "red", offset = 0):
        if self.__win == None:
            return 
        
        fill_colour = fill_colour if not undo else "grey"

        center_position_x = (self._x1 + self._x2) / 2 + offset
        center_position_y = (self._y1 + self._y2) / 2 + offset
        to_cell_center_position_x = (to_cell._x1 + to_cell._x2) / 2 + offset
        to_cell_center_position_y = (to_cell._y1 + to_cell._y2) / 2 + offset

        self.__win.draw_line(Line(Point(center_position_x, center_position_y), Point(to_cell_center_position_x, to_cell_center_position_y)), fill_colour)
