# Program 89: Sequential number triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def main():
    try:
        n = int(input("Enter number of rows: "))
        num = 1
        for i in range(1, n + 1):
            row = []
            for _ in range(i):
                row.append(str(num))
                num += 1
            print(" ".join(row))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
