def apply_operations(value, operations):
    result = value
    for operation in operations:
        result = operation(result)
    return result

def double(x): return x * 2
def add_ten(x): return x + 10

print(apply_operations(5, [double, add_ten, double]))  # Ausgabe: 40