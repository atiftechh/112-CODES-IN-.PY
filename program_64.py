# Program 64: Compute: 1! + 2! + 3! + ... + N!
def main():
    try:
        n = int(input("Enter N: "))
        if n < 1:
            print("N must be at least 1.")
            return
        total = 0
        curr_fact = 1
        for i in range(1, n + 1):
            curr_fact *= i
            total += curr_fact
        print(f"Sum of factorials 1! + 2! + ... + {n}! is: {total}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
