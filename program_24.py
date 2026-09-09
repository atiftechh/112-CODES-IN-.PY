# Program 24: Login Validator : Check whether username and password combination is valid.
def main():
    CORRECT_USER = "admin"
    CORRECT_PASS = "Pass@123"

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == CORRECT_USER and password == CORRECT_PASS:
        print("Login successful! Welcome.")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
