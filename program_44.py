# Program 44: Print numbers from N to 1
def main():
    try:
        n = int(input("Enter N: "))
        print(f"Numbers from {n} down to 1:")
        for i in range(n, 0, -1):
            print(i, end=" ")
        print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
