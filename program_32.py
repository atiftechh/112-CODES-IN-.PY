# Program 32: Check if number is positive, negative, or zero — then if positive check even/odd
def main():
    try:
        n = int(input("Enter an integer: "))
        if n > 0:
            if n % 2 == 0:
                print(f"{n} is Positive and Even.")
            else:
                print(f"{n} is Positive and Odd.")
        elif n < 0:
            print(f"{n} is Negative.")
        else:
            print("The number is Zero.")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
