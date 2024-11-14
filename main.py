def fibonacci(n):
  """Generiert die ersten n Fibonacci-Zahlen."""
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib_zahlen = [0, 1]
    for i in range(2, n):
      fib_zahlen.append(fib_zahlen[i-1] + fib_zahlen[i-2])
    return fib_zahlen

print(fibonacci(10))