from graphics import Line, Point
from typing import Self


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

    def __repr__(self):
        string = f"Cell(has_left_wall={self.has_left_wall}, has_right_wall={self.has_right_wall}, "
        string += f"has_top_wall={self.has_top_wall}, has_bottom_wall={self.has_bottom_wall}, "
        string += f"x1={self._x1}, y1={self._y1}, x2={self._x2}, y2={self._y2})"
        return string

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

    def draw_move(self, to_cell: Self, undo=False):
        path_color = "#00FFFF"
        if undo:
            path_color = "#FF0000"
        from_center = Point((self._x2 - self._x1)//2 + self._x1, (self._y2 - self._y1)//2 + self._y1)
        to_center = Point((to_cell._x2 - to_cell._x1)//2 + to_cell._x1,
                          (to_cell._y2 - to_cell._y1)//2 + to_cell._y1)
        path = Line(from_center, to_center)
        self._win.draw_line(path, path_color)
