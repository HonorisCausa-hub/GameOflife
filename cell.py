import random

class Cell:

    def __init__(self, ix, iy, is_live):
        self.ix = ix
        self.iy = iy
        self.is_live = is_live
        self.neighbour_count = 0

    def __str__(self):
        return "[{},{},{:5}]".format(self.ix, self.iy, str(self.is_live))

    # верхний левый угол - (0,0)
    def calc_neighbour_count(self):
        count = 0
        pre_x = self.ix - 1 if self.ix > 0 else 0
        for i in range(pre_x, self.ix+1+1):
            pre_y = self.iy - 1 if self.iy > 0 else 0
            for j in range(pre_y, self.iy+1+1):
                if i == self.ix and j == self.iy:
                    continue
                if self.invalidate(i, j):
                    continue
                count += int(CellGrid.cells[i][j].is_live)
        self.neighbour_count = count
        return count

    def invalidate(self, x, y):
        if x >= CellGrid.cx or y >= CellGrid.cy:
            return True
        if x < 0 or y < 0:
            return True
        return False

    def rule(self):
        if self.neighbour_count > 3 or self.neighbour_count < 2:
            self.is_live = False
        elif self.neighbour_count == 3:
            self.is_live = True
        elif self.neighbour_count == 2:
            pass


class CellGrid:

    cells = []
    cx = 0
    cy = 0

    def __init__(self, cx, cy):
        CellGrid.cx = cx
        CellGrid.cy = cy
        for i in range(cx):
            cell_list = []
            for j in range(cy):
                cell = Cell(i, j, random.random() > 0.5)
                cell_list.append(cell)
            CellGrid.cells.append(cell_list)

    def circulate_rule(self):
        for cell_list in CellGrid.cells:
            for item in cell_list:
                item.rule()

    def circulate_nbcount(self):
        for cell_list in CellGrid.cells:
            for item in cell_list:
                item.calc_neighbour_count()
