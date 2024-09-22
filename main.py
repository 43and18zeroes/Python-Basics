def safe_int_conversion(value):
    try:
        result = int(value)
        return result
    except ValueError:
        print("Invalid input: Could not convert to integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")