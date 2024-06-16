from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
                self.p1.x, self.p1.y,
                self.p2.x, self.p2.y,
                fill=fill_color, width=2
        )


class Window:
    def __init__(self, width, height):
        self.__root = Tk(className="Maze Solver")
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.wm_protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int,
                 left_wall: bool = True, right_wall: bool = True,
                 top_wall: bool = True, bottom_wall: bool = True,
                 win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # Top left corner
        self._x1 = x1
        self._y1 = y1
        # Top right corner
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(wall, "#00FF00")
        if self.has_right_wall:
            wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(wall, "#00FF00")
        if self.has_top_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(wall, "#00FF00")
        if self.has_bottom_wall:
            wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(wall, "#00FF00")
