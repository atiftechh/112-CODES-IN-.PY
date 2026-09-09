# Program 77: Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order.
def print_inc_dec(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_inc_dec(n, current + 1)
    print(current, end=" ")

def main():
    try:
        n = int(input("Enter positive integer N: "))
        if n < 1:
            print("N must be >= 1.")
            return
        print(f"Pattern for N = {n}:")
        print_inc_dec(n)
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
