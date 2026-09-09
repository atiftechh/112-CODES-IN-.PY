# Program 10: Check if a character is uppercase, lowercase, digit, or special character
def main():
    ch = input("Enter a character: ")
    if len(ch) != 1:
        print("Please enter exactly one character.")
        return
    if 'A' <= ch <= 'Z':
        print(f"'{ch}' is an uppercase letter.")
    elif 'a' <= ch <= 'z':
        print(f"'{ch}' is a lowercase letter.")
    elif '0' <= ch <= '9':
        print(f"'{ch}' is a digit.")
    else:
        print(f"'{ch}' is a special character.")

if __name__ == "__main__":
    main()
