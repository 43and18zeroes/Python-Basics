def my_function(*args, **kwargs):
    print(args)  # Tuple aller positional arguments
    print(kwargs)  # Dictionary aller keyword arguments

my_function(1, 2, 3, a=4, b=5)