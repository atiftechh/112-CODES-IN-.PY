# Program 87: Sandglass / Hourglass
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******
def main():
    try:
        n = int(input("Enter half-height n (e.g. 4): "))
        # Inverted pyramid
        for i in range(n, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        # Regular pyramid starting from 2
        for i in range(2, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
