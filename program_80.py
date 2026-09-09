# Program 80: Right-aligned triangle
#    *
#   **
#  ***
# ****
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
