def durchschnitt(zahlen):
  """Berechnet den Durchschnitt einer Liste von Zahlen."""
  if not zahlen:
    return None
  summe = sum(zahlen)
  anzahl = len(zahlen)
  durchschnitt = summe / anzahl
  return durchschnitt

zahlen = [1, 2, 3, 4, 5]
print(durchschnitt(zahlen))