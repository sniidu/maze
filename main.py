from window import Window
from maze import Maze
from point import Point
from line import Line
from cell import Cell


if __name__ == "__main__":
    # win = Window(800, 600)

    # Testing linedraw
    # p1 = Point(0, 1)
    # p2 = Point(100, 300)
    # line = Line(p1, p2)
    #
    # win.draw_line(line, "white")
    #
    # p1 = Point(200, 100)
    # p2 = Point(0, 600)
    # line = Line(p1, p2)
    #
    # win.draw_line(line, "green")

    # Testing cells draw
    # c = Cell(win)
    # p1 = Point(10, 100)
    # p2 = Point(300, 200)
    # c.draw(p1, p2)
    #
    # c = Cell(win)
    # c.has_top_wall = False
    # c.has_left_wall = False
    # p1 = Point(10, 220)
    # p2 = Point(400, 400)
    # c.draw(p1, p2)

    # Testing cells draw_move
    # c = Cell(win)
    # p1 = Point(10, 100)
    # p2 = Point(300, 200)
    # c.draw(10, 100, 300, 200)
    #
    # c2 = Cell(win)
    # p3 = Point(10, 220)
    # p4 = Point(400, 400)
    # c2.draw(10, 220, 400, 400)

    # c.draw_move(c2)

    # Testing maze
    win2 = Window(800, 600)
    m = Maze(100, 100, 10, 10, 20, 20, win2)

    win2.wait_for_close()
    # m = Maze(
    #     100,
    #     100,
    #     10,
    #     10,
    #     10,
    #     10,
    # )
    # m._break_walls_r(0, 0)
