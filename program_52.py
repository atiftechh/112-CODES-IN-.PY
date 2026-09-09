# Program 52: Happy Number: Repeatedly replace a number with sum of squares of its digits. Determine if it reaches 1.
def sum_of_squared_digits(n):
    total = 0
    while n > 0:
        d = n % 10
        total += d * d
        n //= 10
    return total

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squared_digits(n)
    return n == 1

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        if is_happy(n):
            print(f"{n} is a Happy Number!")
        else:
            print(f"{n} is not a Happy Number.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
