# Program 95: Column-wise incrementing
# 1
# 1 2
# 1 2 3
# 1 2 3 4
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            print(" ".join(str(j) for j in range(1, i + 1)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
