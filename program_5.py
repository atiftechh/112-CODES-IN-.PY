# Program 5: Divisibility Check : Check whether a number is divisible by 3, 5, both, or neither.
def main():
    try:
        n = int(input("Enter an integer: "))
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} is divisible by both 3 and 5.")
        elif n % 3 == 0:
            print(f"{n} is divisible by 3 only.")
        elif n % 5 == 0:
            print(f"{n} is divisible by 5 only.")
        else:
            print(f"{n} is divisible by neither 3 nor 5.")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
