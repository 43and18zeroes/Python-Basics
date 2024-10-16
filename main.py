def ist_palindrom(wort):
  """Überprüft, ob ein Wort ein Palindrom ist."""
  wort = wort.lower()
  return wort == wort[::-1]

print(ist_palindrom("radar"))