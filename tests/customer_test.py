import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub.stock_drinks()
        self.customer = Customer("Timmy", 20, 21)

    def test_customer_has_a_name(self):
        result = self.customer.name
        self.assertEqual("Timmy", result)
    
    def test_customer_has_a_wallet(self):
        result = self.customer.wallet
        self.assertEqual(20, result)


    def test_customer_is_drunk(self):
        self.pub.sell_with_id_check(self.customer, "Rum")
        self.assertEqual(10, self.customer.drunkeness)
