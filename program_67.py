# Program 67: Check if a number is an Armstrong number (generalized for any digits)
def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        num_str = str(n)
        num_digits = len(num_str)
        total = sum(int(d) ** num_digits for d in num_str)
        if total == n:
            print(f"{n} is an Armstrong number (order {num_digits}).")
        else:
            print(f"{n} is not an Armstrong number (calculated sum = {total}).")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
