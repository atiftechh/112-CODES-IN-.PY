# Program 65: Print the multiplication table of a given number
def main():
    try:
        num = int(input("Enter number: "))
        limit = int(input("Enter limit (e.g. 10 or 20): "))
        print(f"--- Multiplication Table for {num} ---")
        for i in range(1, limit + 1):
            print(f"{num} x {i:2d} = {num * i}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
