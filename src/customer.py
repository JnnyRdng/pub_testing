class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkness(self, amount):
        self.drunkeness += amount