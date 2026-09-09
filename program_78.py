# Program 78: Right-angled triangle (stars)
# *
# **
# ***
# ****
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            print("*" * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
