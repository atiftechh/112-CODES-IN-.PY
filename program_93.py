# Program 93: Number pyramid (centered)
#       1
#     1 2 3
#   1 2 3 4 5
# 1 2 3 4 5 6 7
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            spaces = "  " * (n - i)
            nums = " ".join(str(x) for x in range(1, 2 * i))
            print(spaces + nums)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
