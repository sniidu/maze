from tkinter import Tk, Canvas
from line import Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze")

        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)
