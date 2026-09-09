# Program 48: Count the number of digits in a number
def main():
    try:
        n = int(input("Enter an integer: "))
        num = abs(n)
        if num == 0:
            count = 1
        else:
            count = 0
            while num > 0:
                count += 1
                num //= 10
        print(f"Number of digits in {n}: {count}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
