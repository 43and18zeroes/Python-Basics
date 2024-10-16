def fakultaet(n):
  """Berechnet die Fakultät einer nicht-negativen ganzen Zahl."""
  if n < 0:
    return "Die Fakultät ist für negative Zahlen nicht definiert."
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n+1):
      result *= i
    return result

print(fakultaet(5))