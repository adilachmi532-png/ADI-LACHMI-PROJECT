

from Securities import Stock, Bond, Option

def main():
    print("=== Securities Summary ===")

    stock = Stock(
        input("Stock ID: ").strip(),
        float(input("Stock unit price: ")),
        int(input("Units held: ")),
        float(input("Dividend per unit (quarterly): "))
    )

    bond = Bond(
        input("\nBond ID: ").strip(),
        float(input("Bond unit price: ")),
        int(input("Units held: ")),
        float(input("Annual rate (e.g. 0.05): "))
    )

    option = Option(
        input("\nOption ID: ").strip(),
        float(input("Underlying unit price: ")),
        int(input("Units held: ")),
        float(input("Strike price: "))
    )

    print("\n--- Portfolio Report ---")
    print(f"[STOCK]  {stock.asset_id} | Value: {stock.position_value():,.2f} | Annual Dividend: {stock.annual_dividend():,.2f}")
    print(f"[BOND]   {bond.asset_id} | Value: {bond.position_value():,.2f} | Annual Interest: {bond.annual_interest_income():,.2f}")
    print(f"[OPTION] {option.asset_id} | Value: {option.position_value():,.2f} | Status: {'ITM' if option.is_in_the_money() else 'OTM'}")

if __name__ == "__main__":
    main()
