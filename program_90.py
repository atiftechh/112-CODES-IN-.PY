# Program 90: Floyd's triangle
# 1
# 2  3
# 4  5  6
# 7  8  9  10
def main():
    try:
        n = int(input("Enter number of rows for Floyd's Triangle: "))
        val = 1
        for i in range(1, n + 1):
            for j in range(i):
                print(f"{val:2d}", end=" ")
                val += 1
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
