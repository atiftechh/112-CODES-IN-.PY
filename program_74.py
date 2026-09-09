# Program 74: Find the sum of a series: x − x³/3! + x⁵/5! − x⁷/7! ... (sin series)
import math

def sin_series(x, terms):
    # Convert x in degrees or radians (assuming x in radians)
    total = 0.0
    for n in range(terms):
        power = 2 * n + 1
        term = ((-1) ** n) * (x ** power) / math.factorial(power)
        total += term
    return total

def main():
    try:
        x = float(input("Enter x (in radians): "))
        terms = int(input("Enter number of terms (e.g. 10): "))
        approx = sin_series(x, terms)
        actual = math.sin(x)
        print(f"Series approximation: {approx:.8f}")
        print(f"math.sin({x}) value : {actual:.8f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
