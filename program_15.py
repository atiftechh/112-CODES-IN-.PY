# Program 15: Count the number of set bits in a number
def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print(f"Binary representation: {bin(n)}")
            print(f"Number of set bits (in two's complement Python representation): {bin(n).count('1')}")
        else:
            print(f"Binary: {bin(n)[2:]}")
            print(f"Number of set bits: {count_set_bits(n)}")
    except ValueError:
        print("Invalid integer.")

if __name__ == "__main__":
    main()
