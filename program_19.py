# Program 19: Find the largest of three numbers
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))
        if a >= b and a >= c:
            largest = a
        elif b >= a and b >= c:
            largest = b
        else:
            largest = c
        print(f"The largest of the three numbers is: {largest}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
