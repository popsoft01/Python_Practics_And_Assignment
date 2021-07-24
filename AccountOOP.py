from decimal import Decimal


class Account:
    def __init__(self, firstName, lastName, balance):

        if balance > Decimal(0.0):
            self.balance = balance
        else:
            raise ValueError("Illegal balance")
        self.firstName = firstName
        self.lastName = lastName

    def deposit(self, amount):
        if amount > 0.0:
            self.balance += amount
        else:
            raise TypeError("invalid amount")

    def withdraw(self, amount):


tunde = Account("Tunde", "Pop", 1000)
tunde.deposit(2000)
print(str(tunde))
