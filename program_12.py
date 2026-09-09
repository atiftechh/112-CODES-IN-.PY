# Program 12: Swap two numbers using XOR
def main():
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))
        print(f"Before swap: a = {a}, b = {b}")
        a = a ^ b
        b = a ^ b
        a = a ^ b
        print(f"After swap: a = {a}, b = {b}")
    except ValueError:
        print("Invalid integers.")

if __name__ == "__main__":
    main()
