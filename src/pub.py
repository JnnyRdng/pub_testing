from src.drink import Drink

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def stock_drinks(self):
        self.drinks.append(Drink("Vodka", 5))
        self.drinks.append(Drink("Rum", 4))
        self.drinks.append(Drink("Champagne", 26))