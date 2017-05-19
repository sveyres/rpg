#!/usr/bin/env python
# -- coding: UTF-8 --
from core.character import Player
from core.item import Rock

import unittest

class TestPlayer(unittest.TestCase):

    def testPick(self):
        item = Rock(10)
        item1 = Rock(15)
        player = Player(50, 5)
        player.pick(item)
        self.assertTrue(item in player.inventory.items)
        player.pick(item1)
        self.assertFalse(item1 in player.inventory.items)

    def testDrop(self):
        item = Rock(10)
        player = Player(50, 5)
        player.pick(item)
        player.drop(item)
        self.assertFalse(item in player.inventory.items)

    def testFight(self):
        player = Player(50, 5)
        enemy = Player(50, 5)

        player.fight(enemy)
        player.fight(enemy)
        player.fight(enemy)
        self.assertTrue(enemy.health == 20)

    def testReceiveAttack(self):
        player = Player(50, 5)
        player.receive_attack(10)
        player.receive_attack(10)
        self.assertTrue(player.health == 30)


if __name__ == '__main__':
    unittest.main()
