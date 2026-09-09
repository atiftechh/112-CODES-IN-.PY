# Program 20: Check if a character is a vowel or consonant
def main():
    ch = input("Enter an alphabet character: ").strip()
    if len(ch) != 1 or not ch.isalpha():
        print("Please enter a single alphabetic character.")
        return
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{ch}' is a vowel.")
    else:
        print(f"'{ch}' is a consonant.")

if __name__ == "__main__":
    main()
