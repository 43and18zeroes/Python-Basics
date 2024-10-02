def apply_to_all(func, iterable):
    return [func(item) for item in iterable]

numbers = [1, 2, 3, 4]
squared = apply_to_all(lambda x: x**2, numbers)