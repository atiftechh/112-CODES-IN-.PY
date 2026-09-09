# Program 108: Right arrow pattern
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
def main():
    try:
        n = int(input("Enter arrow head width (e.g. 4): "))
        for i in range(1, n + 1):
            print("* " * i)
        for i in range(n - 1, 0, -1):
            print("* " * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
