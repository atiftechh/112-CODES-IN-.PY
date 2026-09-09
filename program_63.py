# Program 63: Find x^n (power) without using built-in pow function
def power(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / power(x, -n)
    res = 1.0
    base = x
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            res *= base
        base *= base
        exp //= 2
    return res

def main():
    try:
        x = float(input("Enter base x: "))
        n = int(input("Enter integer exponent n: "))
        ans = power(x, n)
        print(f"{x}^{n} = {ans}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
