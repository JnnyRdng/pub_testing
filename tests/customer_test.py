import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Timmy", 20)

    def test_customer_has_a_name(self):
        result = self.customer.name
        self.assertEqual("Timmy", result)
    
    def test_customer_has_a_wallet(self):
        result = self.customer.wallet
        self.assertEqual(20, result)
        



# A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till