# Program 18: Find the largest of two numbers
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if a > b:
            print(f"Largest number is: {a}")
        elif b > a:
            print(f"Largest number is: {b}")
        else:
            print("Both numbers are equal.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
