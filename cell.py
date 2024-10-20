from window import Window
from point import Point
from line import Line


class Cell:
    def __init__(
        self,
        win: Window | None = None,
    ) -> None:
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if not self._win:
            return

        left_line = Line(Point(x1, y1), Point(x1, y2))
        left_wall_color = "black" if self.has_left_wall else "#323232"
        self._win.draw_line(left_line, fill_color=left_wall_color)

        top_line = Line(Point(x1, y1), Point(x2, y1))
        top_wall_color = "black" if self.has_top_wall else "#323232"
        self._win.draw_line(top_line, fill_color=top_wall_color)

        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        bottom_wall_color = "black" if self.has_bottom_wall else "#323232"
        self._win.draw_line(bottom_line, fill_color=bottom_wall_color)

        right_line = Line(Point(x2, y1), Point(x2, y2))
        right_wall_color = "black" if self.has_right_wall else "#323232"
        self._win.draw_line(right_line, fill_color=right_wall_color)

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        if not self._win:
            return

        if not self._x1:
            raise Exception("Can't move as self coordinates are missing - draw first")

        c1_middle = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        c2_middle = Point(
            (to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2
        )

        line = Line(c1_middle, c2_middle)
        color = "red" if undo else "gray"
        self._win.draw_line(line, color)
