# Program 13: Find the value of n << 1 and n >> 1 — relate to multiply/divide by 2
def main():
    try:
        n = int(input("Enter an integer: "))
        left_shift = n << 1
        right_shift = n >> 1
        print(f"n << 1 = {left_shift} (Equivalent to {n} * 2 = {n * 2})")
        print(f"n >> 1 = {right_shift} (Equivalent to {n} // 2 = {n // 2})")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
