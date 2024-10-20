from cell import Cell
from window import Window
import random
import time


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()

    def _create_cells(self):
        self._cells = []
        for _ in range(self._num_cols):
            cells: list[Cell] = []
            for _ in range(self._num_rows):
                cells.append(Cell(self._win))
            self._cells.append(cells)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(row, col)

    def _draw_cell(self, i, j):
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[j][i].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return

        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self) -> None:
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        entrance.draw(entrance._x1, entrance._y1, entrance._x2, entrance._y2)
        exit.draw(exit._x1, exit._y1, exit._x2, exit._y2)

    def _break_walls_r(self, i: int, j: int) -> None:
        """Knock down walls until all cells are visited
        works firstly in depth and continues in breadth"""
        c = self._cells[j][i]
        c.visited = True

        while True:
            # check all adjacent cells
            # mind the boundaries
            directions = []
            if j - 1 >= 0 and not self._cells[j - 1][i].visited:
                directions.append(("up", i, j - 1))
            if j + 1 <= self._num_cols - 1 and not self._cells[j + 1][i].visited:
                directions.append(("down", i, j + 1))
            if i + 1 <= self._num_rows - 1 and not self._cells[j][i + 1].visited:
                directions.append(("right", i + 1, j))
            if i - 1 >= 0 and not self._cells[j][i - 1].visited:
                directions.append(("left", i - 1, j))

            # in case no possible routings, just draw and return
            # should end up here for all cells
            if len(directions) == 0:
                self._draw_cell(i, j)
                return

            # next direction and cell
            next = random.randrange(len(directions))
            next_direction, next_i, next_j = directions[next]

            next_cell = self._cells[next_j][next_i]

            if next_direction == "up":
                c.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_direction == "down":
                c.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif next_direction == "right":
                c.has_right_wall = False
                next_cell.has_left_wall = False
            else:
                c.has_left_wall = False
                next_cell.has_right_wall = False

            # for checking on how maze creates
            # self._draw_cell(i, j)

            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self) -> None:
        """Reset visited property for all cells"""
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        """Depth first solver for maze"""
        self._animate()

        c = self._cells[j][i]
        c.visited = True

        if j == self._num_cols - 1 and i == self._num_rows - 1:
            return True

        if j - 1 >= 0 and not self._cells[j - 1][i].visited and not c.has_top_wall:
            c.draw_move(self._cells[j - 1][i])
            if self._solve_r(i, j - 1):
                return True
            else:
                c.draw_move(self._cells[j - 1][i], undo=True)

        if (
            j + 1 <= self._num_cols - 1
            and not self._cells[j + 1][i].visited
            and not c.has_bottom_wall
        ):
            c.draw_move(self._cells[j + 1][i])
            if self._solve_r(i, j + 1):
                return True
            else:
                c.draw_move(self._cells[j + 1][i], undo=True)
        if (
            i + 1 <= self._num_rows - 1
            and not self._cells[j][i + 1].visited
            and not c.has_right_wall
        ):
            c.draw_move(self._cells[j][i + 1])
            if self._solve_r(i + 1, j):
                return True
            else:
                c.draw_move(self._cells[j][i + 1], undo=True)
        if i - 1 >= 0 and not self._cells[j][i - 1].visited and not c.has_left_wall:
            c.draw_move(self._cells[j][i - 1])
            if self._solve_r(i - 1, j):
                return True
            else:
                c.draw_move(self._cells[j][i - 1], undo=True)

        return False
