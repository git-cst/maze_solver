from tkinter import Tk, BOTH, Canvas
from constants import ACCEPTED_FILL_COLOURS, WINDOW_COLOUR, MAZE_LINE_WIDTH

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, fill_colour: str) -> None:
        if fill_colour not in ACCEPTED_FILL_COLOURS:
            raise ValueError(f"Non-accepted fill colour was passed. Accepted fill colours are {ACCEPTED_FILL_COLOURS}")
        
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_colour, width=MAZE_LINE_WIDTH)

class Window():
    def __init__(self, window_size: tuple[int, int]):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze solver")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas_widget = Canvas(master=self.__root_widget, bg=WINDOW_COLOUR, width=window_size[0], height=window_size[1])
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


