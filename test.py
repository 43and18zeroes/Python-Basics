set_var = {12, 28, 38, True, 29, "Florian"}
print(set_var) # {'Florian', True, 29, 38, 12, 28} Sets haben keine feste Reihenfolge

set_var2 = {1, 2, 1}
print(set_var2) # {1, 2} Es wird kein Fehler geworfen, das Duplikat wird einfach nicht berücksichtigt

set_var3 = {1, 2, 3}
print(len(set_var3)) # 3

set_var4 = {1, 2, 1}
print(len(set_var4)) # 2 Duplikate werden nicht mitgezählt

liste = [42, "Florian", True]
print(len(liste))