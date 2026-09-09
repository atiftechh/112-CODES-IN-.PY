# Program 7: Check if a number is positive, negative, or zero
def main():
    try:
        n = float(input("Enter a number: "))
        if n > 0:
            print(f"{n} is positive.")
        elif n < 0:
            print(f"{n} is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
