# Program 98: Alphabet triangle (row repeat)
# A
# B B
# C C C
# D D D D
def main():
    try:
        n = int(input("Enter number of rows (1-26): "))
        n = min(n, 26)
        for i in range(n):
            ch = chr(ord('A') + i)
            print(" ".join([ch] * (i + 1)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
