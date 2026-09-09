# Program 29: Given 3 sides, check if a valid triangle can be formed
def main():
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))

        if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
            print("Yes, a valid triangle can be formed.")
        else:
            print("No, these sides cannot form a valid triangle.")
    except ValueError:
        print("Invalid numerical input.")

if __name__ == "__main__":
    main()
