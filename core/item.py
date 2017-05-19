#!/usr/bin/env python
# -- coding: UTF-8 --

class Item(object):
    def __init__(self, weight):
        self.weight = weight

    def use(self):
        pass

class Weapon(Item):

    def __init__(self, weight, damage):
        Item.__init__(self, weight)
        self.damage = damage

    def use(self):
        return self.damage

class Rock(Item):

    def __init__(self, weight):
        Item.__init__(self, weight)
        self.damage = 10

class Armor(Item):
    def __init__(self, weight, defence):
        Item.__init__(self, weight)
        self.defence = defence

    def use(self):
        return self.defence

class Shield(Item):
    def __init__(self, weight, defence):
        Item.__init__(self, weight)
        self.defence = defence

    def use(self):
        return self.defence

class Helmet(Item):
    def __init__(self, weight, defence):
        Item.__init__(self, weight)
        self.defence = defence

    def use(self):
        return self.defence

class Food(Item):

    def __init__(self, weight, gain):
        Item.__init__(self, weight)
        self.gain = gain
    def use():
        pass

class Inventory(object):
    def __init__(self, size):
        self.size = size
        self.items = []

    def get_item(self, item):
        if item in self.items:
           return item
        return None

    def set_item(self, item):
        invent_weight = sum(item.weight for item in self.items)
        if invent_weight + item.weight <= self.size:
            self.items.append(item)
            return True
        return False

    def del_item(self, item):
        if item in self.items:
           self.items.pop(self.items.index(item))
           return True
        return False
