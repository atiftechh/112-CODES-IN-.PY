# Program 28: Check if a triangle is equilateral, isosceles, or scalene given 3 sides
def main():
    try:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Side lengths must be positive.")
        elif a + b <= c or a + c <= b or b + c <= a:
            print("The sides do not form a valid triangle.")
        elif a == b == c:
            print("Triangle is Equilateral.")
        elif a == b or b == c or a == c:
            print("Triangle is Isosceles.")
        else:
            print("Triangle is Scalene.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
