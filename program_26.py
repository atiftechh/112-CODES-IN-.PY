# Program 26: Read a number (1–7) and print the corresponding day of the week
def main():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    try:
        n = int(input("Enter day number (1-7): "))
        if n in days:
            print(f"Day {n} is {days[n]}.")
        else:
            print("Invalid input! Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid number.")

if __name__ == "__main__":
    main()
