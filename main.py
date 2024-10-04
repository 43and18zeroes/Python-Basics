def fibonacci(n):
    """Gibt die n-te Fibonacci-Zahl zurück."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Gib eine Zahl ein: "))
for i in range(n):
    print(fibonacci(i))