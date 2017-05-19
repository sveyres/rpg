#!/usr/bin/env python
# -- coding: UTF-8 --
from core.board import Board, Cell
from core.character import Player
from core.display import BoardDisplayer

import unittest
import inspect

class TestDisplay(unittest.TestCase):

    def testBoardDisplayerDecorator(self):
        board = Board(50, 50)
        player = Player(50, 1)

        self.assertTrue(issubclass(BoardDisplayer, Board))

        decorated_board = BoardDisplayer(board, player)
        self.assertTrue(board.get_grid() == decorated_board.get_grid())
        self.assertTrue(board.get_height() == decorated_board.get_height())
        self.assertTrue(board.get_width() == decorated_board.get_width())
        self.assertTrue(hasattr(decorated_board, "display"))
        self.assertTrue(inspect.ismethod(decorated_board.display))
        self.assertTrue(hasattr(decorated_board, "wait_move"))
        self.assertTrue(inspect.ismethod(decorated_board.wait_move))


if __name__ == '__main__':
    unittest.main()
