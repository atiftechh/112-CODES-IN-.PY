# Program 97: Binary number triangle
# 0
# 0 1
# 0 1 0
# 0 1 0 1
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            row = [str(j % 2) for j in range(i)]
            print(" ".join(row))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
