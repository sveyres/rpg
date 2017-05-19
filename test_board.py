#!/usr/bin/env python
# -- coding: UTF-8 --
from core.board import Board, Cell

import unittest

class TestBoard(unittest.TestCase):

    def testBoardInitialisation(self):
        board = Board(50, 50)
        self.assertTrue(len(board.grid) == 50)
        for lig in range(50):
            self.assertTrue(len(board.grid[lig]) == 50)
            for col in range(50):
                cell = board.grid[lig][col]
                self.assertTrue(isinstance(cell, Cell))

    def testBoardGetGrid(self):
        board = Board(50, 50)
        board_grid = board.get_grid()
        self.assertTrue(len(board.grid[0]) == len(board_grid[0]))
        self.assertTrue(len(board.grid) == len(board_grid))
        for lig in range(50):
            for col in range(50):
                self.assertTrue(board.grid[lig][col] == board_grid[lig][col])


    def testBoardGetCell(self):
        board = Board(50, 50)
        for lig in range(50):
            for col in range(50):
                cell = board.get_cell(lig, col)
                self.assertTrue(isinstance(cell, Cell))
                self.assertTrue(cell.lig == lig)
                self.assertTrue(cell.col == col)

    def testBoardGetDimension(self):
        board = Board(24, 42)
        self.assertTrue(board.get_height() == 24)
        self.assertTrue(board.get_width() == 42)


if __name__ == '__main__':
    unittest.main()
