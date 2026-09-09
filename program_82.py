# Program 82: Pyramid (centered)
#    *
#   ***
#  *****
# *******
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
