# Program 39: Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5x rate)
def main():
    try:
        hours = float(input("Enter total hours worked: "))
        rate = float(input("Enter hourly rate: "))

        if hours <= 0 or rate <= 0:
            print("Hours and rate must be positive.")
            return

        if hours <= 40:
            salary = hours * rate
        else:
            regular_pay = 40 * rate
            overtime_hours = hours - 40
            overtime_pay = overtime_hours * (rate * 1.5)
            salary = regular_pay + overtime_pay

        print(f"Total Salary: Rs. {salary:.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
