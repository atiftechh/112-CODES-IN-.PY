# Program 1: Read two numbers and print their sum, difference, product, quotient, and remainder
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Sum: {a + b}")
        print(f"Difference: {a - b}")
        print(f"Product: {a * b}")
        if b != 0:
            print(f"Quotient: {a / b}")
            print(f"Remainder: {a % b}")
        else:
            print("Division and remainder by zero are undefined.")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()
