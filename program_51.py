# Program 51: Check if a number is a palindrome
def main():
    try:
        n = int(input("Enter an integer: "))
        if n < 0:
            print(f"{n} is not a palindrome (negative numbers cannot be palindromes).")
            return
        temp = n
        rev = 0
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10
        if rev == n:
            print(f"{n} is a palindrome.")
        else:
            print(f"{n} is not a palindrome.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
