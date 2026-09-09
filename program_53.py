# Program 53: Product of Digits: Find the product of all digits of a number using recursion.
def product_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

def main():
    try:
        num = int(input("Enter an integer: "))
        print(f"Product of digits of {num} is: {product_of_digits(num)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
