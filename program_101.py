# Program 101: Right-aligned alphabet triangle
#       A
#     A B
#   A B C
# A B C D
def main():
    try:
        n = int(input("Enter number of rows (1-26): "))
        n = min(n, 26)
        for i in range(1, n + 1):
            spaces = "  " * (n - i)
            letters = " ".join(chr(ord('A') + j) for j in range(i))
            print(spaces + letters)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
