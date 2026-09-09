# Program 69: Print all factors / divisors of a number
import math

def main():
    try:
        n = int(input("Enter an integer: "))
        num = abs(n)
        if num == 0:
            print("0 has infinitely many divisors.")
            return
        factors = set()
        for i in range(1, math.isqrt(num) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        print(f"Factors/Divisors of {n}: {sorted(factors)}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
