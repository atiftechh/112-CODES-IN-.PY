# Program 14: Check if the Kth bit of a number is set or not (0-indexed from right)
def main():
    try:
        n = int(input("Enter the number: "))
        k = int(input("Enter bit position k (0-indexed): "))
        if (n >> k) & 1:
            print(f"Bit at position {k} is SET (1).")
        else:
            print(f"Bit at position {k} is NOT SET (0).")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
