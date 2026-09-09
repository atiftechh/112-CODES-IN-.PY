# Program 36: Read cost price and selling price — print profit, loss, or no profit no loss
def main():
    try:
        cp = float(input("Enter Cost Price (CP): "))
        sp = float(input("Enter Selling Price (SP): "))
        if sp > cp:
            profit = sp - cp
            pct = (profit / cp) * 100 if cp != 0 else 0
            print(f"Profit: Rs. {profit:.2f} ({pct:.2f}%)")
        elif cp > sp:
            loss = cp - sp
            pct = (loss / cp) * 100 if cp != 0 else 0
            print(f"Loss: Rs. {loss:.2f} ({pct:.2f}%)")
        else:
            print("No Profit, No Loss.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
