# Program 59: Find LCM of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        ans = lcm(a, b)
        print(f"LCM of {a} and {b} is: {ans}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
