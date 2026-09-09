# Program 3: Calculate simple interest given P, R, T → (P × R × T) / 100
def main():
    try:
        p = float(input("Enter Principal amount: "))
        r = float(input("Enter Rate of interest (per year %): "))
        t = float(input("Enter Time period (years): "))
        si = (p * r * t) / 100
        print(f"Simple Interest: {si:.2f}")
        print(f"Total Amount: {(p + si):.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
