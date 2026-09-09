# Program 47: Calculate the sum of first N natural numbers
def main():
    try:
        n = int(input("Enter N: "))
        if n < 1:
            print("N must be a positive integer.")
            return
        total = n * (n + 1) // 2
        print(f"Sum of first {n} natural numbers is: {total}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
