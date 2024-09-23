def safe_division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")def safe_division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")