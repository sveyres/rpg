#!/usr/bin/env python
# -- coding: UTF-8 -

from core.display import *
from core.character import *
from core.board import *


board = Board(20, 20)
player = Player(50, 1)
boardDisplayer = ConsoleBoard(board, player)

boardDisplayer.display()
    # new_cell = boardDisplayer.wait_move()
    # player.move(new_cell)
