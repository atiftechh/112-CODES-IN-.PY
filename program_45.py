# Program 45: Print all even numbers from 1 to N
def main():
    try:
        n = int(input("Enter N: "))
        print(f"Even numbers from 1 to {n}:")
        for i in range(2, n + 1, 2):
            print(i, end=" ")
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
