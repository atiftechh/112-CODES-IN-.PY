# Program 38: Check if a 3-digit number is an Armstrong number (e.g., 153)
def main():
    try:
        n = int(input("Enter a 3-digit number: "))
        if n < 100 or n > 999:
            print("Please enter a valid 3-digit number.")
            return
        temp = n
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** 3
            temp //= 10
        if total == n:
            print(f"{n} is an Armstrong number.")
        else:
            print(f"{n} is not an Armstrong number (Sum of cubes is {total}).")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
