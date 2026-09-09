# Program 46: Print all odd numbers from 1 to N
def main():
    try:
        n = int(input("Enter N: "))
        print(f"Odd numbers from 1 to {n}:")
        for i in range(1, n + 1, 2):
            print(i, end=" ")
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
