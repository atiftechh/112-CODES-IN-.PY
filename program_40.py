# Program 40: ATM Withdrawal : Approve or reject withdrawal based on amount, balance, and minimum-balance rules.
def main():
    try:
        balance = float(input("Enter current account balance: "))
        min_balance = float(input("Enter minimum required balance: "))
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")
        elif balance - amount < min_balance:
            print("Transaction Rejected: Insufficient balance to maintain minimum balance requirement.")
        else:
            balance -= amount
            print(f"Transaction Approved! Please collect Rs. {amount:.2f}")
            print(f"Remaining Balance: Rs. {balance:.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
