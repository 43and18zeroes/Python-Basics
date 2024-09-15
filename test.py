tupel = (2, 3, 7, 4, 7)

n = tupel.count(7)
print(n) # 2

print(tupel.index(3)) # 1

kopie = tupel.copy()
print(kopie) # [8, 3, 8]

print(list(tupel)) # [2, 3, 7, 4, 7], Casting

liste = list(tupel)
liste.sort()
print(liste) # [2, 3, 4, 7, 7]

