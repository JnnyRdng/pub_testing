from src.drink import Drink

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def stock_drinks(self):
        self.drinks.append(Drink("Vodka", 5, 12))
        self.drinks.append(Drink("Rum", 4, 10))
        self.drinks.append(Drink("Champagne", 26, 6))

    def find_drink(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink

    def add_to_till(self, amount):
        self.till += amount

    def sell_with_no_id_check(self, customer, order):
        drink = self.find_drink(order)
        self.add_to_till(drink.price)
        customer.reduce_wallet(drink.price)

    def check_id(self, customer):
        return customer.age >= 18

    def sell_with_id_check(self, customer, order):
        if self.check_id(customer):
            drink = self.find_drink(order)
            self.add_to_till(drink.price)
            customer.reduce_wallet(drink.price)
            customer.increase_drunkness(drink.alcohol_level)
