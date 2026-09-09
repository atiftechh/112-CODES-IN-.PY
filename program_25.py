# Program 25: Given marks (0–100), print grade: A (>=90), B (>=80), C (>=70), D (>=60), F (<60)
def main():
    try:
        marks = float(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Invalid marks! Must be between 0 and 100.")
        elif marks >= 90:
            print("Grade: A")
        elif marks >= 80:
            print("Grade: B")
        elif marks >= 70:
            print("Grade: C")
        elif marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
