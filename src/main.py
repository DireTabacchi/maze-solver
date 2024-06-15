from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(50, 100)), "#00FF00")
    win.draw_line(Line(Point(200, 300), Point(400, 300)), "#00FF00")
    win.wait_for_close()


main()
