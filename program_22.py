# Program 22: Age Category : Classify person as child, teenager, adult, or senior based on age.
def main():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Invalid age.")
        elif age <= 12:
            print("Category: Child")
        elif age <= 19:
            print("Category: Teenager")
        elif age <= 59:
            print("Category: Adult")
        else:
            print("Category: Senior Citizen")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
