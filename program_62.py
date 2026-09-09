# Program 62: Compute: 1 − 2 + 3 − 4 + 5 − ... up to N terms
def main():
    try:
        n = int(input("Enter N: "))
        if n <= 0:
            print("N must be positive.")
            return
        # If n is even, sum = -n // 2. If n is odd, sum = (n + 1) // 2
        total = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                total += i
            else:
                total -= i
        print(f"Sum of alternating series up to {n} terms is: {total}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
