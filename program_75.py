# Program 75: Palindrome Check: Check whether a string is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def main():
    s = input("Enter a string: ").strip()
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    if is_palindrome(cleaned):
        print(f"'{s}' is a Palindrome!")
    else:
        print(f"'{s}' is NOT a Palindrome.")

if __name__ == "__main__":
    main()
