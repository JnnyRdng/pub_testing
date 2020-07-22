import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.stock_drinks()
        self.customer = Customer("Timmy", 20, 21)

    def test_pub_has_name(self):
        result = self.pub.name
        self.assertEqual("The Prancing Pony", result)

    def test_pub_has_cash(self):
        result = self.pub.till
        self.assertEqual(100.00, result)

    def test_pub_has_drinks(self):
        result = len(self.pub.drinks)
        self.assertEqual(3, result)

    def test_stock_drinks(self):
        result = len(self.pub.drinks)
        self.assertEqual(3, result)

    def test_find_drink_in_list(self):
        result = self.pub.find_drink("Vodka")
        self.assertEqual("Vodka", result.name)

    def test_customer_can_buy_drink(self):
        self.pub.sell_with_no_id_check(self.customer, "Vodka")
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(15, self.customer.wallet)

    def test_customer_can_pass_id_check(self):
        result = self.pub.check_id(self.customer)
        self.assertEqual(True, result)

    def test_underage_cant_buy_drink(self):
        teenager = Customer("Billy", 50, 16)
        self.pub.sell_with_id_check(teenager, "Rum")
        self.assertEqual(50, teenager.wallet)

    def test_customer_too_drunk(self):
        self.customer.drunkeness = 30
        self.pub.sell_with_id_check(self.customer, "Champage")
        self.assertEqual(20, self.customer.wallet)

        