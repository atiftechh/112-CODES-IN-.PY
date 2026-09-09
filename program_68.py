# Program 68: Find the largest and smallest digit in a number
def main():
    try:
        n = int(input("Enter an integer: "))
        digits = [int(d) for d in str(abs(n))]
        print(f"Largest digit: {max(digits)}")
        print(f"Smallest digit: {min(digits)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
