from Invoice import Invoice

def main():
    print("=== Invoice System ===")

    invoice_id = input("Invoice ID: ")
    customer_name = input("Customer name: ")
    issue_date = input("Issue date: ")
    vat_rate = float(input("VAT rate (e.g. 0.17): "))
    is_paid = False

    invoice = Invoice(
        invoice_id,
        customer_name,
        issue_date,
        vat_rate,
        is_paid
    )

    print("\n--- Invoice Amount ---")
    net_amount = float(input("Net amount: "))
    discount = float(input("Discount (0 if none): "))

    print("\n--- Invoice Summary ---")
    invoice.print_invoice(net_amount, discount)

if __name__ == "__main__":
    main()
