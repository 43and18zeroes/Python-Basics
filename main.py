def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 120:
        raise ValueError("Age seems unrealistic.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except ValueError as e:
    print(e)