from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cells = []
    for i in range(16):
        cell = Cell(win=win)
        if i & 1 == 1:
            cell.has_top_wall = False
        if i & 2 == 2:
            cell.has_right_wall = False
        if i & 4 == 4:
            cell.has_bottom_wall = False
        if i & 8 == 8:
            cell.has_left_wall = False
        cells.append(cell)
    x = 20
    y = 20
    for i in range(16):
        if i % 4 == 0 and i != 0:
            x = 20
            y += 40
        cells[i].draw(x, y, x+20, y+20)
        x += 40
    win.wait_for_close()


main()
