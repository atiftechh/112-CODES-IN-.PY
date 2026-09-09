# Program 71: Convert decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    n = abs(n)
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return ("-" if is_negative else "") + binary

def main():
    try:
        n = int(input("Enter a decimal integer: "))
        print(f"Binary representation: {decimal_to_binary(n)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
