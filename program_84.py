# Program 84: Diamond shape
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def main():
    try:
        n = int(input("Enter half-height n (e.g. 4): "))
        # Top half + middle
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        # Bottom half
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
