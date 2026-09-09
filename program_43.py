# Program 43: Print numbers from 1 to N
def main():
    try:
        n = int(input("Enter N: "))
        print(f"Numbers from 1 to {n}:")
        for i in range(1, n + 1):
            print(i, end=" ")
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
