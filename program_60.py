# Program 60: Print Fibonacci series up to N terms
def main():
    try:
        n = int(input("Enter number of terms N: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        a, b = 0, 1
        print(f"Fibonacci series ({n} terms):")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
