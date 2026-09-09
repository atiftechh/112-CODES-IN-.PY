# Program 102: Alphabet pyramid (centered)
#       A
#     A B A
#   A B C B A
# A B C D C B A
def main():
    try:
        n = int(input("Enter number of rows (1-26): "))
        n = min(n, 26)
        for i in range(1, n + 1):
            spaces = "  " * (n - i)
            first_half = [chr(ord('A') + j) for j in range(i)]
            second_half = [chr(ord('A') + j) for j in range(i - 2, -1, -1)]
            print(spaces + " ".join(first_half + second_half))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
