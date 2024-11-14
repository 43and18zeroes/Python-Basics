def ist_primzahl(zahl):
  """Überprüft, ob eine Zahl eine Primzahl ist."""
  if zahl <= 1:
    return False
  if zahl <= 3:
    return True
  if zahl % 2 == 0 or zahl % 3 == 0:
    return False
  i = 5
  while i * i <= zahl:
    if zahl % i == 0 or zahl % (i + 2) == 0:
      return False
    i += 6
  return True

print(ist_primzahl(17))