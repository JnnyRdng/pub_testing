import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Timmy", 20)
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.stock_drinks()

    def test_customer_has_a_name(self):
        result = self.customer.name
        self.assertEqual("Timmy", result)
    
    def test_customer_has_a_wallet(self):
        result = self.customer.wallet
        self.assertEqual(20, result)

    def test_customer_can_buy_drink(self):
        drink = self.pub.find_drink("Vodka")
        self.pub.till += drink.price
        self.customer.wallet -= drink.price
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(15, self.customer.wallet)

        



# A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till