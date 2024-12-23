from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def calculate(self, price):
        return price - (price * self.percentage / 100)

class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def calculate(self, price):
        return price - self.amount

def apply_discount(price, discount):
    return discount.calculate(price)

discount = PercentageDiscount(10)
print(apply_discount(100, discount))  