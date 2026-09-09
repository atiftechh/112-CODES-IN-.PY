# Program 54: Extract and print each digit of a number from left to right
def main():
    try:
        s = input("Enter an integer: ").strip()
        if s.startswith('-'):
            print(f"Negative sign: -")
            s = s[1:]
        print("Digits from left to right:")
        for ch in s:
            if ch.isdigit():
                print(ch, end=" ")
        print()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
