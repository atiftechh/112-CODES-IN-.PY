# Program 33: Given 3 numbers, print them in ascending order using only if-else
def main():
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        c = float(input("Enter third number (c): "))

        if a <= b and a <= c:
            first = a
            if b <= c:
                second, third = b, c
            else:
                second, third = c, b
        elif b <= a and b <= c:
            first = b
            if a <= c:
                second, third = a, c
            else:
                second, third = c, a
        else:
            first = c
            if a <= b:
                second, third = a, b
            else:
                second, third = b, a

        print(f"Numbers in ascending order: {first}, {second}, {third}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
