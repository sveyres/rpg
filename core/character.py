#!/usr/bin/env python
# -- coding: UTF-8 --
#
from core.item import Inventory

class Character(object):

    def __init__(self, health, xp):
        self.health = health
        self.xp = xp

    def move(self):
        pass

    def eat(self, food):
        sefl.health += food.use()

    def die(self):
        pass

    def receive_attack(self, damage):
        self.health -= damage

class Player(Character):

    def __init__(self, health, xp):
        Character.__init__(self, health, xp)
        self.inventory = Inventory(20)

    def pick(self, item):
        self.inventory.set_item(item)

    def drop(self, item):
        self.inventory.del_item(item)

    def fight(self, character):
        damage = 10
        character.receive_attack(damage)

    def receive_attack(self, damage):
        Character.receive_attack(self,damage)

class Chicken(Character):

    def __init__(self, health, xp):
        Character.__init___(30, 1)
