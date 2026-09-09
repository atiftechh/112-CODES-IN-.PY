# Program 105: Number diamond
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1
#   1 2 3 2 1
#     1 2 1
#       1
def print_row(i, n):
    spaces = "  " * (n - i)
    left = [str(x) for x in range(1, i + 1)]
    right = [str(x) for x in range(i - 1, 0, -1)]
    print(spaces + " ".join(left + right))

def main():
    try:
        n = int(input("Enter peak number n (e.g. 4): "))
        for i in range(1, n + 1):
            print_row(i, n)
        for i in range(n - 1, 0, -1):
            print_row(i, n)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
