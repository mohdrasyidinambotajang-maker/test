# Basic exception handling
try:
    number = int(input("Enter a integer number: "))
    result = 10/number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! enter integer number")
except ZeroDivisionError:
    print("Cannot divide by 0")

# Raising exceptions
def validate_age(age):
    if age < 1:
        raise ValueError("Your are not born yet")
    if age > 150:
        raise ValueError("Are you ghost?")
    return True


try:
    age = int(input("Enter your age: "))
    validate_age(age)
except ValueError as e:
    print(f"Validation error: {e}")