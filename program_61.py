# Program 61: Compute the sum: 1 + 1/2 + 1/3 + ... + 1/N
def main():
    try:
        n = int(input("Enter N: "))
        if n <= 0:
            print("N must be a positive integer.")
            return
        total = sum(1 / i for i in range(1, n + 1))
        print(f"Harmonic sum up to {n} terms is: {total:.6f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
