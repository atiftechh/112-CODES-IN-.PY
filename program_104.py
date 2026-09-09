# Program 104: Hollow diamond inside rectangle
# * * * * * * *
# * * *   * * *
# * *       * *
# *           *
# * *       * *
# * * *   * * *
# * * * * * * *
def main():
    try:
        n = int(input("Enter size n (e.g. 4): "))
        total_rows = 2 * n - 1
        for i in range(total_rows):
            k = i if i < n else 2 * n - 2 - i
            stars = n - k
            spaces = 2 * k - 1
            if spaces <= 0:
                print("*" * (2 * n - 1))
            else:
                print("*" * stars + " " * spaces + "*" * stars)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
