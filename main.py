def ggt(a, b):
  """Berechnet den größten gemeinsamen Teiler zweier Zahlen."""
  while b != 0:
    a, b = b, a % b
  return a

print(ggt(48, 18))