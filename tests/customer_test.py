import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Timmy", 20, 21)

    def test_customer_has_a_name(self):
        result = self.customer.name
        self.assertEqual("Timmy", result)
    
    def test_customer_has_a_wallet(self):
        result = self.customer.wallet
        self.assertEqual(20, result)


        

