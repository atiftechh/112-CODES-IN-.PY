# Program 55: Find factorial of N
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def main():
    try:
        n = int(input("Enter a non-negative integer N: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"{n}! = {factorial(n)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
