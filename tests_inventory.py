#!/usr/bin/env python
# -- coding: UTF-8 --
from core.item import Item, Weapon, Rock, Armor, Shield, Helmet, Food, Inventory

import unittest


class TestItems(unittest.TestCase):

    def testItemConstructor(self):
        with self.assertRaises(TypeError):
            Item()
        with self.assertRaises(TypeError):
            Item(42, "plop")
        item = Item(12)
        self.assertEqual(item.weight, 12)

    def testWeaponConstructor(self):
        with self.assertRaises(TypeError):
            Weapon()
        with self.assertRaises(TypeError):
            Weapon(42)
        weapon = Weapon(12, 42)
        self.assertEqual(weapon.weight, 12)
        self.assertEqual(weapon.damage, 42)

    def testRockConstructor(self):
        with self.assertRaises(TypeError):
            Rock()
        with self.assertRaises(TypeError):
            Rock(10, 42)
        rock = Rock(42)
        self.assertEqual(rock.weight, 42)
        self.assertEqual(rock.damage, 10)  # constant

    def testArmorConstructor(self):
        with self.assertRaises(TypeError):
            Armor()
        with self.assertRaises(TypeError):
            Armor(42)
        armor = Armor(10, 42)
        self.assertEqual(armor.weight, 10)
        self.assertEqual(armor.defence, 42)

    def testShieldConstructor(self):
        self.testArmorConstructor()

    def testHelmetConstructor(self):
        self.testArmorConstructor()

    def testFoodConstructor(self):
        with self.assertRaises(TypeError):
            Food()
        with self.assertRaises(TypeError):
            Food(42)
        food = Food(10, 42)
        self.assertEqual(food.weight, 10)
        self.assertEqual(food.gain, 42)


class TestInventory(unittest.TestCase):

    def testInventoryConstructor(self):
        with self.assertRaises(TypeError):
            Inventory()
        inventory = Inventory(10)
        self.assertEqual(inventory.size, 10)
        self.assertEqual(inventory.items, [])

    def testInventorySetItem(self):
        inventory = Inventory(30)
        food = Food(10, 42)

        inventory.set_item(food)
        self.assertTrue(food in inventory.items)

    def testInventoryGetItem(self):
        inventory = Inventory(30)
        food = Food(10, 42)

        inventory.set_item(food)
        res = inventory.get_item(food)
        self.assertEqual(food, res)

    def testInventoryDelItem(self):
        inventory = Inventory(30)
        food = Food(10, 42)
        food2 = Food(10, 42)
        inventory.set_item(food)

        res = inventory.del_item(food)
        self.assertTrue(res)
        self.assertTrue(food not in inventory.items)

        res = inventory.del_item(food2)
        self.assertFalse(res)

    def testInventoryFull(self):
        inventory = Inventory(30)
        res = inventory.set_item(Food(10, 42))
        self.assertTrue(res)
        res = inventory.set_item(Food(10, 42))
        self.assertTrue(res)
        food = Food(15, 42)
        res = inventory.set_item(Food(15, 42))
        self.assertFalse(res)
        self.assertFalse(food in inventory.items)


if __name__ == '__main__':
    unittest.main()
