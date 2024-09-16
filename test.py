zahlen = {1, 4, 6, 8}

zahlen.add(-1) # {1, 4, 6, 8, -1}
print(zahlen)

zahlen.remove(1)
print(zahlen) # {4, 6, 8, -1}

kopie = zahlen.copy()
print(kopie)

zahlen.clear()
print(zahlen) # set()