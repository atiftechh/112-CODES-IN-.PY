# Program 9: Read age and check eligibility to vote (age ≥ 18)
def main():
    try:
        age = int(input("Enter age: "))
        if age >= 18:
            print("Eligible to vote.")
        elif age >= 0:
            print(f"Not eligible to vote. Wait for {18 - age} more year(s).")
        else:
            print("Age cannot be negative.")
    except ValueError:
        print("Invalid age entered.")

if __name__ == "__main__":
    main()
