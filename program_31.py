# Program 31: Read month number (1–12) and print number of days in that month
def main():
    try:
        month = int(input("Enter month number (1-12): "))
        if month in [1, 3, 5, 7, 8, 10, 12]:
            print("Number of days: 31")
        elif month in [4, 6, 9, 11]:
            print("Number of days: 30")
        elif month == 2:
            year = int(input("Enter year (to check leap year for Feb): "))
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                print("Number of days: 29 (Leap Year)")
            else:
                print("Number of days: 28")
        else:
            print("Invalid month number! Enter between 1 and 12.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
