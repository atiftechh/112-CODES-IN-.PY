# Program 8: Read three numbers and check if all three are equal (use and)
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        if a == b and b == c:
            print("All three numbers are equal.")
        else:
            print("The three numbers are not all equal.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
