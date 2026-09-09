# Program 21: Ticket Pricing : Calculate ticket price based on customer's age.
def main():
    try:
        age = int(input("Enter customer's age: "))
        if age < 0:
            print("Invalid age.")
            return
        if age < 5:
            price = 0  # Free for infants/toddlers
        elif age <= 12:
            price = 50  # Child rate
        elif age <= 60:
            price = 100 # Adult rate
        else:
            price = 70  # Senior citizen concession
        print(f"Ticket Price: Rs. {price}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
