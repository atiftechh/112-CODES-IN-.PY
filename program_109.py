# Program 109: X pattern
# *     *
#  *   *
#    *
#  *   *
# *     *
def main():
    try:
        n = int(input("Enter odd size n (e.g. 5): "))
        for i in range(n):
            for j in range(n):
                if j == i or j == (n - 1 - i):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
