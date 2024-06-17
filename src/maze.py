from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
               col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if i + 1 < self._num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j + 1 < self._num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_cell = to_visit[random.randrange(len(to_visit))]
            if next_cell[1] < j:
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            if next_cell[0] > i:
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            if next_cell[1] > j:
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            if next_cell[0] < i:
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
                self._cells[i][j].has_left_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        next_moves_lst = []
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            next_moves_lst.append((i, j-1))
        if i + 1 < self._num_cols and not self._cells[i+1][j].visited:
            next_moves_lst.append((i+1, j))
        if j + 1 < self._num_rows and not self._cells[i][j+1].visited:
            next_moves_lst.append((i, j+1))
        if i - 1 >= 0 and not self._cells[i-1][j].visited:
            next_moves_lst.append((i-1, j))
        
        for move in next_moves_lst:
            # Check for top move
            if (move[1] < j 
                and not self._cells[i][j].has_top_wall
                and not self._cells[move[0]][move[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[move[0]][move[1]])
                is_end = self._solve_r(move[0], move[1])
                if is_end:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[move[0]][move[1]], undo=True)
            # check for right move
            if (move[0] > i
                and not self._cells[i][j].has_right_wall
                and not self._cells[move[0]][move[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[move[0]][move[1]])
                is_end = self._solve_r(move[0], move[1])
                if is_end:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[move[0]][move[1]], undo=True)
            # Check for bottom move
            if (move[1] > j
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[move[0]][move[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[move[0]][move[1]])
                is_end = self._solve_r(move[0], move[1])
                if is_end:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[move[0]][move[1]], undo=True)
            # Check for left move
            if (move[0] < i
                and not self._cells[i][j].has_left_wall
                and not self._cells[move[0]][move[1]].visited
            ):
                self._cells[i][j].draw_move(self._cells[move[0]][move[1]])
                is_end = self._solve_r(move[0], move[1])
                if is_end:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[move[0]][move[1]], undo=True)

        return False


