# Program 110: Plus (+) pattern
#     *
#     *
# * * * * *
#     *
#     *
def main():
    try:
        n = int(input("Enter odd size n (e.g. 5): "))
        mid = n // 2
        for i in range(n):
            for j in range(n):
                if i == mid or j == mid:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
