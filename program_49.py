# Program 49: Find the sum of digits of a number
def main():
    try:
        n = int(input("Enter an integer: "))
        num = abs(n)
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        print(f"Sum of digits of {n} is: {s}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
