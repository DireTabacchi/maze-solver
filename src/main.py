from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cells = []
    for i in range(16):
        cells.append(Cell(win))
    cells[0].has_left_wall = False
    cells[0].has_right_wall = False
    cells[1].has_left_wall = False
    cells[1].has_right_wall = False
    cells[2].has_left_wall = False
    cells[2].has_bottom_wall = False
    cells[3].has_right_wall = False
    cells[3].has_bottom_wall = False
    cells[4].has_bottom_wall = False
    cells[5].has_right_wall = False
    cells[6].has_top_wall = False
    cells[6].has_bottom_wall = False
    cells[6].has_left_wall = False
    cells[7].has_top_wall = False
    cells[7].has_bottom_wall = False
    cells[8].has_top_wall = False
    cells[8].has_right_wall = False
    cells[9].has_right_wall = False
    cells[9].has_bottom_wall = False
    cells[9].has_left_wall = False
    cells[10].has_top_wall = False
    cells[10].has_bottom_wall = False
    cells[10].has_left_wall = False
    cells[11].has_top_wall = False
    cells[11].has_bottom_wall = False
    cells[12].has_right_wall = False
    cells[13].has_top_wall = False
    cells[13].has_left_wall = False
    cells[14].has_top_wall = False
    cells[14].has_right_wall = False
    cells[15].has_top_wall = False
    cells[15].has_left_wall = False
    
    x = 20
    y = 20
    for i in range(16):
        if i % 4 == 0:
            x = 20
            y += 20
        cells[i].draw(x, y, x+20, y+20)
        x += 20

    cells[0].draw_move(cells[1])
    cells[1].draw_move(cells[2])
    cells[2].draw_move(cells[6])
    cells[6].draw_move(cells[5], undo=True)
    cells[6].draw_move(cells[10])
    cells[10].draw_move(cells[9], undo=True)
    cells[9].draw_move(cells[8], undo=True)
    cells[8].draw_move(cells[4], undo=True)
    cells[10].draw_move(cells[14])
    cells[14].draw_move(cells[15])
    cells[15].draw_move(cells[11])
    cells[11].draw_move(cells[7])
    cells[7].draw_move(cells[3])
    win.wait_for_close()


main()
