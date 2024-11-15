def wort_zaehle(text):
  """Zählt die Wörter in einem Text."""
  woerter = text.split()
  anzahl_woerter = len(woerter)
  return anzahl_woerter

text = "Dies ist ein Beispieltext zur Wortzählung."
print(wort_zaehle(text))