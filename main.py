class InvalidInputError(Exception):
    pass

def validate_input(value):
    if not value.isdigit():
        raise InvalidInputError("Input must be a digit.")

try:
    input_value = input("Enter a digit: ")
    validate_input(input_value)
    print("Input is valid.")
except InvalidInputError as e:
    print(e)