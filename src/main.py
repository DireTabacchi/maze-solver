from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    m = Maze(20, 20, 8, 8, 20, 20, win)
    win.wait_for_close()


main()
