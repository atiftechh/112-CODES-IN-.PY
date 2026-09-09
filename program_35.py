# Program 35: Check if a given character is an alphabet, digit, or special character
def main():
    s = input("Enter a character: ")
    if len(s) != 1:
        print("Please enter exactly one character.")
        return
    ch = s[0]
    if ch.isalpha():
        print(f"'{ch}' is an Alphabet.")
    elif ch.isdigit():
        print(f"'{ch}' is a Digit.")
    else:
        print(f"'{ch}' is a Special Character.")

if __name__ == "__main__":
    main()
