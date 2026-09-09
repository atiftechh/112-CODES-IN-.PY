# Program 100: Reverse alphabet triangle
# A B C D
# A B C
# A B
# A
def main():
    try:
        n = int(input("Enter number of rows (1-26): "))
        n = min(n, 26)
        for i in range(n, 0, -1):
            print(" ".join(chr(ord('A') + j) for j in range(i)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
