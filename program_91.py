# Program 91: 1-0 alternating triangle
# 1
# 1 0
# 1 0 1
# 1 0 1 0
def main():
    try:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            for j in range(i):
                print(1 if j % 2 == 0 else 0, end=" ")
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
