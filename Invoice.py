class Invoice:
    def __init__(self, invoice_id, customer_name, issue_date, vat_rate, is_paid):
        self.__invoice_id = invoice_id       
        self._customer_name = customer_name  
        self._issue_date = issue_date
        self._vat_rate = vat_rate            
        self._is_paid = is_paid

   
    
    def invoice_id(self):
        return self.__invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        value = str(value).strip()
        if value != "":
            self.__invoice_id = value

    
    def customer_name(self):
        return self._customer_name


    def customer_name(self, value):
        value = str(value).strip()
        if value != "":
            self._customer_name = value

    def vat_rate(self):
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, value):
      
        if 0 <= value <= 1:
            self._vat_rate = value

    
    def total_with_vat(self, net_amount, discount=0.0):
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
