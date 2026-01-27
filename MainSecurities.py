from Securities import Stock, Bond, Option

def main():
    stock = Stock(
        input("Stock name: "),
        float(input("Stock price: ")),
        int(input("Stock qty: ")),
        float(input("Dividend: "))
    )

    bond = Bond(
        input("\nBond name: "),
        float(input("Bond price: ")),
        int(input("Bond qty: ")),
        float(input("Interest: "))
    )

    option = Option(
        input("\nOption name: "),
        float(input("Option price: ")),
        int(input("Option qty: ")),
        float(input("Strike: "))
    )

    print("\n--- Results ---")
    print("Stock value:", stock.value())
    print("Dividend:", stock.yearly_dividend())

    print("Bond value:", bond.value())
    print("Interest:", bond.yearly_interest())

    print("Option value:", option.value())
    print("Profitable?:", option.is_profitable())

if __name__ == "__main__":
    main()
