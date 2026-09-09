# Program 94: Inverted number triangle
# 1 2 3 4
# 1 2 3
# 1 2
# 1
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(n, 0, -1):
            print(" ".join(str(j) for j in range(1, i + 1)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
