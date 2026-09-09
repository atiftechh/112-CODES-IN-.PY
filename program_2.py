# Program 2: Calculate the area of a circle given radius (A = πr²)
import math

def main():
    try:
        r = float(input("Enter radius of the circle: "))
        if r < 0:
            print("Radius cannot be negative.")
        else:
            area = math.pi * r * r
            print(f"Area of circle: {area:.4f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
