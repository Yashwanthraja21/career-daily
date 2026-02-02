try:
    Numerator = float(input("Enter the Numerator: "))
    Denominator = float(input("Enter the Denominator: "))
    value = Numerator / Denominator
    print(value)

except ValueError:
    print("Invalid Input, Enter the number")

except ZeroDivisionError:
    print("Invalid Input, Enter the number higher than zero")
