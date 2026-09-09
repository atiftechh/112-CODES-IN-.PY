# Program 79: Inverted right-angled triangle
# ****
# ***
# **
# *
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(n, 0, -1):
            print("*" * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
