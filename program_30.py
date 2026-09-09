# Program 30: Build a simple calculator (+, −, ×, ÷) using switch-case (match-case)
def main():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        match op:
            case '+':
                print(f"{num1} + {num2} = {num1 + num2}")
            case '-':
                print(f"{num1} - {num2} = {num1 - num2}")
            case '*':
                print(f"{num1} * {num2} = {num1 * num2}")
            case '/':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("Invalid operator entered.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
