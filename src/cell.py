from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        # Top left corner
        self._x1 = None
        self._y1 = None
        # Top right corner
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        # Top left corner
        self._x1 = x1
        self._y1 = y1
        # Top right corner
        self._x2 = x2
        self._y2 = y2
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
