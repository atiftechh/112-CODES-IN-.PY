# Program 73: Read numbers until user enters −1, print the count and average
def main():
    print("Enter numbers one by one (enter -1 to stop):")
    total = 0
    count = 0
    while True:
        try:
            val = float(input("Enter number: "))
            if val == -1:
                break
            total += val
            count += 1
        except ValueError:
            print("Invalid input, please enter a valid number.")

    if count > 0:
        avg = total / count
        print(f"Count of numbers: {count}")
        print(f"Sum of numbers: {total}")
        print(f"Average: {avg:.4f}")
    else:
        print("No numbers were entered before -1.")

if __name__ == "__main__":
    main()
