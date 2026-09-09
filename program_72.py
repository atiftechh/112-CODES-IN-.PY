# Program 72: Convert binary to decimal
def binary_to_decimal(b_str):
    total = 0
    power = 0
    for ch in reversed(b_str):
        if ch not in ('0', '1'):
            raise ValueError("Invalid binary digit.")
        total += int(ch) * (2 ** power)
        power += 1
    return total

def main():
    b_str = input("Enter a binary number: ").strip()
    try:
        dec = binary_to_decimal(b_str)
        print(f"Decimal equivalent: {dec}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
