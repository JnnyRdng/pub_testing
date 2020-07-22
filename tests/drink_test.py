import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Guinness", 3.50)

    def test_drink_has_a_name(self):
        result = self.drink.name
        self.assertEqual("Guinness", result)

    def test_drink_has_price(self):
        result = self.drink.price
        self.assertEqual(3.50, result)