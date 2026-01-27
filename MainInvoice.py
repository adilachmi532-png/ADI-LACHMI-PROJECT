from Invoice import Invoice

def main():
  
    number = input("Enter invoice number: ")
    customer = input("Enter customer name: ")
    date = input("Enter date: ")
    vat = float(input("Enter VAT: "))
    paid = False

    
    inv = Invoice(number, customer, date, vat, paid)


    print("Invoice number:", inv.number)
    print("Customer:", inv.customer)


    amount = float(input("Enter amount: "))
    inv.print_invoice(amount)

if __name__ == "__main__":
    main()
