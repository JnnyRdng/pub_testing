import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        result = self.pub.name
        self.assertEqual("The Prancing Pony", result)

    def test_pub_has_cash(self):
        result = self.pub.till
        self.assertEqual(100.00, result)

    def test_pub_has_no_drinks(self):
        result = len(self.pub.drinks)
        self.assertEqual(0, result)