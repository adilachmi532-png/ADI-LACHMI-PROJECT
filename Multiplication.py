
def Multiplication(a, b):
    if a == 0 or b == 0:
        return False
    return a % b == 0 or b % a == 0


def main():
    while True:
        try:
            x = int(input("First: "))
            if x == -1:
                print("Exit")
                break

            y = int(input("Second: "))
            if y == -1:
                print("Exit")
                break

            print("YES" if Multiplication(x, y) else "NO")

        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
