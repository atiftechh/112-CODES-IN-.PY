# Program 17: Check if a year is a leap year
def main():
    try:
        year = int(input("Enter year: "))
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid year.")

if __name__ == "__main__":
    main()
