#!/usr/bin/env python
# -- coding: UTF-8 --

from core.board import *
from core.character import *


class BoardDisplayer(Board):
    def __init__(self, board, player):
        self.grid = board.get_grid()
        self.player = player

    def display(self):
        pass

    def wait_move(self):
        pass

class ConsoleBoard(BoardDisplayer):

    def display(self):
        res = ""
        lig = self.get_height()
        col = self.get_width()
        for l in range(lig):
            for c in range(col):
                cell = self.get_cell(l, c)
                if self.player in cell.characters:
                    res += "X "
                else:
                    res += "# "
            res += "\n"
        print res
