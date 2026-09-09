# Program 66: Find the sum of even and odd numbers separately from 1 to N
def main():
    try:
        n = int(input("Enter N: "))
        even_sum = sum(i for i in range(2, n + 1, 2))
        odd_sum = sum(i for i in range(1, n + 1, 2))
        print(f"Sum of even numbers from 1 to {n}: {even_sum}")
        print(f"Sum of odd numbers from 1 to {n}: {odd_sum}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
