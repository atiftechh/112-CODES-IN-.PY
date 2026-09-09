# Program 88: Number triangle (row-wise)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            print(" ".join([str(i)] * i))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
