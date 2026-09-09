# Program 76: Count Vowels: Count the number of vowels in a string using recursion.
def count_vowels(s):
    if not s:
        return 0
    is_vowel = 1 if s[0].lower() in 'aeiou' else 0
    return is_vowel + count_vowels(s[1:])

def main():
    text = input("Enter a string: ")
    cnt = count_vowels(text)
    print(f"Number of vowels in '{text}': {cnt}")

if __name__ == "__main__":
    main()
