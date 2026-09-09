# Program 23: Time Greeting : Given an hour (0-23), print Morning, Afternoon, Evening, or Night.
def main():
    try:
        hour = int(input("Enter hour in 24-hour format (0-23): "))
        if 0 <= hour < 5:
            print("Good Night")
        elif 5 <= hour < 12:
            print("Good Morning")
        elif 12 <= hour < 17:
            print("Good Afternoon")
        elif 17 <= hour < 21:
            print("Good Evening")
        elif 21 <= hour <= 23:
            print("Good Night")
        else:
            print("Invalid hour! Please enter between 0 and 23.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
