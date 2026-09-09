# Program 57: Print all prime numbers from 1 to N
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input("Enter N: "))
        print(f"Prime numbers from 1 to {n}:")
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        print(" ".join(map(str, primes)))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
