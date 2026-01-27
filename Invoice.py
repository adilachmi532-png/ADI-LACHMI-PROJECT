class Invoice:
    def __init__(self, invoice_id, customer_name, issue_date, vat_rate, is_paid):
        self.__invoice_id = invoice_id       # private
        self._customer_name = customer_name  # protected
        self._issue_date = issue_date
        self._vat_rate = vat_rate            # can be 0.17 (17%)
        self._is_paid = is_paid

    # -------- PROPERTY: private --------
    @property
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        value = str(value).strip()
        if value != "":
            self.__invoice_id = value

    # -------- PROPERTY: protected --------
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        value = str(value).strip()
        if value != "":
            self._customer_name = value

    # -------- properties רגילות --------
    @property
    def vat_rate(self):
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, value):
        # keep it simple: allow VAT as 0.0 to 1.0 (e.g., 0.17)
        if 0 <= value <= 1:
            self._vat_rate = value

    # -------- methods (2+) --------
    def total_with_vat(self, net_amount, discount=0.0):
        """
        net_amount: amount before VAT
        discount: discount amount (not percent), default 0
        """
        if net_amount < 0:
            return 0

        if discount < 0:
            discount = 0

        net_after_discount = max(0, net_amount - discount)
        return net_after_discount * (1 + self._vat_rate)

    def print_invoice(self, net_amount, discount=0.0):
        print("Invoice ID:", self.__invoice_id)
        print("Customer:", self._customer_name)
        print("Issue date:", self._issue_date)
        print("Paid:", "Yes" if self._is_paid else "No")
        print("VAT rate:", f"{self._vat_rate * 100:.0f}%")
        print("Total:", self.total_with_vat(net_amount, discount))
