def my_decorator(**kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Vor der Funktionsausführung
            result = func(*args, **kwargs)
            # Nach der Funktionsausführung
            return result
        return wrapper
    return decorator

@my_decorator(log=True)
def my_function(a, b):
    return a + b