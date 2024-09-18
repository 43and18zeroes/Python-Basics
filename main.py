liste = [1, 2, 3, "Flo", "Junus", "Manu"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    print(liste[index])
except IndexError:
    print("Der Zugriff ist fehlgeschlagen.")
    
try:
  x = int(input("Gib eine Zahl ein: "))
  y = int(input("Gib eine andere Zahl ein: "))
  result = x / y
except ValueError:
  print("Bitte gib nur Zahlen ein.")
except ZeroDivisionError:
  print("Division durch Null ist nicht erlaubt!")