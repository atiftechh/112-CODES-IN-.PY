# Program 34: Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)
import cmath
import math

def main():
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("This is a linear equation (a cannot be 0 for quadratic).")
            return

        d = (b ** 2) - (4 * a * c)
        print(f"Discriminant D = {d}")

        if d > 0:
            r1 = (-b + math.sqrt(d)) / (2 * a)
            r2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"Roots are Real and Distinct: {r1:.4f} and {r2:.4f}")
        elif d == 0:
            r = -b / (2 * a)
            print(f"Roots are Real and Equal: {r:.4f}")
        else:
            r1 = (-b + cmath.sqrt(d)) / (2 * a)
            r2 = (-b - cmath.sqrt(d)) / (2 * a)
            print(f"Roots are Complex/Imaginary: {r1} and {r2}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
