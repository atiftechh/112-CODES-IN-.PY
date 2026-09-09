# Program 16: Check if a number is even or odd
def main():
    try:
        n = int(input("Enter an integer: "))
        if n % 2 == 0:
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
