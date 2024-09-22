def divide_integers(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero.") from e

try:
    result = divide_integers(10, 0)
except Exception as e:
    print(e)