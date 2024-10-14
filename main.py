def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Vor dem Funktionsaufruf")
        result = func(*args, **kwargs)
        print("Nach dem Funktionsaufruf")
        return result
    return wrapper

@my_decorator
def my_function(x, y):
    return x + y

print(my_function(3, 4))