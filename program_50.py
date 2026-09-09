# Program 50: Reverse a number
def main():
    try:
        n = int(input("Enter an integer: "))
        sign = -1 if n < 0 else 1
        num = abs(n)
        rev = 0
        while num > 0:
            rev = rev * 10 + (num % 10)
            num //= 10
        rev *= sign
        print(f"Reversed number: {rev}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
