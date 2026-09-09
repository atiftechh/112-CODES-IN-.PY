# Program 27: Calculate electricity bill based on slab rates
# Slab rates:
# First 100 units: Rs. 1.50 per unit
# Next 100 units (101-200): Rs. 2.50 per unit
# Next 100 units (201-300): Rs. 4.00 per unit
# Above 300 units: Rs. 5.00 per unit
def main():
    try:
        units = float(input("Enter units consumed: "))
        if units < 0:
            print("Units cannot be negative.")
            return

        bill = 0
        if units <= 100:
            bill = units * 1.50
        elif units <= 200:
            bill = (100 * 1.50) + ((units - 100) * 2.50)
        elif units <= 300:
            bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
        else:
            bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 5.00)

        print(f"Total Electricity Bill: Rs. {bill:.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
