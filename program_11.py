# Program 11: Check if a number is even or odd using bitwise AND ( n & 1 )
def main():
    try:
        n = int(input("Enter an integer: "))
        if n & 1:
            print(f"{n} is odd.")
        else:
            print(f"{n} is even.")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
