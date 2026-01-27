
class Security:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity



class Stock(Security):
    def __init__(self, name, price, quantity, dividend):
        super().__init__(name, price, quantity)
        self.dividend = dividend

    def yearly_dividend(self):
        return self.dividend * self.quantity


class Bond(Security):
    def __init__(self, name, price, quantity, interest):
        super().__init__(name, price, quantity)
        self.interest = interest

    def yearly_interest(self):
        return self.value() * self.interest



class Option(Security):
    def __init__(self, name, price, quantity, strike_price):
        super().__init__(name, price, quantity)
        self.strike_price = strike_price

    def is_profitable(self):
        return self.price > self.strike_price
