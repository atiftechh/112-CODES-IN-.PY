# Program 70: Check if a number is a perfect number (sum of proper divisors == number)
import math

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 1:
            print(f"{n} is not a perfect number.")
            return
        div_sum = 1
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                div_sum += i
                if i != n // i:
                    div_sum += n // i
        if div_sum == n:
            print(f"{n} is a Perfect Number!")
        else:
            print(f"{n} is not a Perfect Number (sum of proper divisors is {div_sum}).")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
