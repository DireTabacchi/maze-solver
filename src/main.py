from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    #win.draw_line(Line(Point(50, 50), Point(50, 100)), "#00FF00")
    #win.draw_line(Line(Point(200, 300), Point(400, 300)), "#00FF00")
    cells = []
    x = 20
    y = 20
    for i in range(16):
        print(f"{i} % 4 = {i%4}")
        if i % 4 == 0 and i != 0:
            x = 20
            y += 40
        cell = Cell(x, y, x+20, y+20, win=win)
        if i & 1 == 1:
            cell.has_top_wall = False
        if i & 2 == 2:
            cell.has_right_wall = False
        if i & 4 == 4:
            cell.has_bottom_wall = False
        if i & 8 == 8:
            cell.has_left_wall = False
        cells.append(cell)
        x += 40
        print(f"{i}&1: {i&1}")
        print(f"{i}&2: {i&2}")
        print(f"{i}&4: {i&4}")
        print(f"{i}&8: {i&8}")
    for cell in cells:
        cell.draw()
    win.wait_for_close()


main()
