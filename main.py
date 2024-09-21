def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Vor Ausführung der Funktion")
        result = func(*args, **kwargs)
        print("Nach Ausführung der Funktion")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hallo, {name}!")

greet("Welt")