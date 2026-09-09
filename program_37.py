# Program 37: Given coordinates (x, y), determine which quadrant the point lies in
def main():
    try:
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))

        if x > 0 and y > 0:
            print(f"Point ({x}, {y}) lies in Quadrant I.")
        elif x < 0 and y > 0:
            print(f"Point ({x}, {y}) lies in Quadrant II.")
        elif x < 0 and y < 0:
            print(f"Point ({x}, {y}) lies in Quadrant III.")
        elif x > 0 and y < 0:
            print(f"Point ({x}, {y}) lies in Quadrant IV.")
        elif x == 0 and y == 0:
            print("Point is at the Origin (0, 0).")
        elif x == 0:
            print("Point lies on the Y-axis.")
        else:
            print("Point lies on the X-axis.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
