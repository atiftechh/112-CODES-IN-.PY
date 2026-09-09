# Program 58: Find GCD / HCF of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        ans = gcd(abs(a), abs(b))
        print(f"GCD / HCF of {a} and {b} is: {ans}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
