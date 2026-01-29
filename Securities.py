
class Security:
    def __init__(self, asset_id, unit_price, units):
        self.asset_id = asset_id
        self.unit_price = unit_price
        self.units = units

    def position_value(self):
        if self.unit_price < 0 or self.units < 0:
            return 0
        return round(self.unit_price * self.units, 2)


class Stock(Security):
    def __init__(self, asset_id, unit_price, units, dividend_per_unit):
        super().__init__(asset_id, unit_price, units)
        self.dividend_per_unit = dividend_per_unit

    def annual_dividend(self):
        return round(self.dividend_per_unit * self.units * 4, 2)


class Bond(Security):
    def __init__(self, asset_id, unit_price, units, annual_rate):
        super().__init__(asset_id, unit_price, units)
        self.annual_rate = annual_rate

    def annual_interest_income(self):
        return round(self.position_value() * self.annual_rate, 2)


class Option(Security):
    def __init__(self, asset_id, unit_price, units, strike_price):
        super().__init__(asset_id, unit_price, units)
        self.strike_price = strike_price

    def is_in_the_money(self):
        return self.unit_price >= self.strike_price * 1.05
