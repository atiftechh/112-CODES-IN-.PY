# Program 6: Read two numbers and print which is greater (use relational operators)
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if a > b:
            print(f"{a} is greater than {b}.")
        elif b > a:
            print(f"{b} is greater than {a}.")
        else:
            print(f"Both numbers are equal ({a}).")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
