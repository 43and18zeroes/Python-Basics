def bubble_sort(liste):
  """Sortiert eine Liste aufsteigend mit dem Bubble Sort-Algorithmus."""
  n = len(liste)
  for i in range(n):
    for j in range(0, n-i-1):
      if liste[j] > liste[j+1]:
        liste[j], liste[j+1] = liste[j+1], liste[j]
  return liste

liste = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(liste))