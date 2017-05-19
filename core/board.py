#!/usr/bin/env python
# -- coding: UTF-8 --
from item import *
from character import *

class Board(object):
    def __init__(self, lig, col):
        self.grid = []
        for l in range(lig):
            itm = []
            for c in range(col):
                itm.append(Cell(l, c))
            self.grid.append(itm)

    def get_grid(self):
        return self.grid

    def get_cell(self, lig, col):
        return self.grid[lig][col]

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        return len(self.grid[0])

class Cell(Board):
    def __init__(self, lig, col):
        self.lig = lig
        self.col = col
        self.items = []
        self.characters = []
