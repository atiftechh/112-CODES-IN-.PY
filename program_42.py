# Program 42: Scholarship Eligibility : Determine eligibility based on marks, attendance, and family income.
# Criteria:
# Marks >= 85%
# Attendance >= 80%
# Family income <= Rs. 3,00,000 per annum
def main():
    try:
        marks = float(input("Enter marks percentage (0-100): "))
        attendance = float(input("Enter attendance percentage (0-100): "))
        income = float(input("Enter annual family income (in Rs.): "))

        if marks >= 85 and attendance >= 80 and income <= 300000:
            print("Eligible for Scholarship!")
        else:
            reasons = []
            if marks < 85:
                reasons.append("Marks below 85%")
            if attendance < 80:
                reasons.append("Attendance below 80%")
            if income > 300000:
                reasons.append("Family income exceeds Rs. 3,00,000")
            print(f"Not Eligible for Scholarship due to: {', '.join(reasons)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
