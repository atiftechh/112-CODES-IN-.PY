# Program 92: Pascal's triangle
#       1
#     1   1
#   1   2   1
# 1   3   3   1
def main():
    try:
        n = int(input("Enter number of rows: "))
        row = [1]
        for i in range(n):
            print(" " * (n - i - 1) * 2, end="")
            print("   ".join(map(str, row)))
            next_row = [1]
            for j in range(len(row) - 1):
                next_row.append(row[j] + row[j + 1])
            next_row.append(1)
            row = next_row
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
