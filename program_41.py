# Program 41: Clock Angle : Given hour and minute, calculate the smaller angle between the two hands.
def main():
    try:
        h = int(input("Enter hour (1-12): "))
        m = int(input("Enter minute (0-59): "))

        if h < 1 or h > 12 or m < 0 or m > 59:
            print("Invalid time input.")
            return

        # Hour hand moves 0.5 degrees per minute, 30 degrees per hour
        hour_angle = (h % 12) * 30 + m * 0.5
        minute_angle = m * 6

        diff = abs(hour_angle - minute_angle)
        smaller_angle = min(diff, 360 - diff)

        print(f"Smaller angle between hands: {smaller_angle:.2f} degrees")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
