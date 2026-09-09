# Program 96: Reverse number triangle
# 4 3 2 1
# 3 2 1
# 2 1
# 1
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(n, 0, -1):
            print(" ".join(str(j) for j in range(i, 0, -1)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
