class Invoice:
    def __init__(self, number, customer, date, vat, paid):
        self.__number = number      # private
        self._customer = customer   # protected
        self._date = date
        self._vat = vat
        self._paid = paid

    # -------- PROPERTY: private --------
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if value != "":
            self.__number = value

    # -------- PROPERTY: protected --------
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if value != "":
            self._customer = value

    # -------- properties רגילות --------
    @property
    def vat(self):
        return self._vat

    @vat.setter
    def vat(self, value):
        if value >= 0:
            self._vat = value

    # -------- methods (2+) --------
    def total(self, amount):
        return amount * (1 + self._vat)

    def print_invoice(self, amount):
        print("Invoice number:", self.__number)
        print("Customer:", self._customer)
        print("Date:", self._date)
        print("Total:", self.total(amount))
