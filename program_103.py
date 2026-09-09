# Program 103: Butterfly pattern
# *          *
# * *      * *
# * * *  * * *
# * * * ** * *
# * * *  * * *
# * *      * *
# *          *
def main():
    try:
        n = int(input("Enter half-size n (e.g. 4): "))
        # Top half
        for i in range(1, n + 1):
            stars = "*" * i
            spaces = " " * (2 * (n - i))
            print(stars + spaces + stars)
        # Bottom half
        for i in range(n - 1, 0, -1):
            stars = "*" * i
            spaces = " " * (2 * (n - i))
            print(stars + spaces + stars)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
