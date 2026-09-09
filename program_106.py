# Program 106: Zigzag pattern
#   *   *   *
#  * * * * * *
# *   *   *   *
def main():
    try:
        cols = int(input("Enter number of columns (e.g. 9 or 13): "))
        for i in range(1, 4):
            for j in range(1, cols + 1):
                if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
