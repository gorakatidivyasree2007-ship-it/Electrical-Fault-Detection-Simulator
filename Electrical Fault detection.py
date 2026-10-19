limit = float(input("Current limit (A): "))
current = float(input("Measured current (A): "))

if limit <= 0 or current < 0:
    print("Invalid readings")
elif current > limit:
    print("ALERT: Overcurrent detected!")
elif current >= 0.9 * limit:
    print("WARNING: Near current limit")
else:
    print("Current within configured limit")
