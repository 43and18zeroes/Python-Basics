liste = [1, 2, 3, "Flo", "Junus", "Manu"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    print(liste[index])
except Exception:
    print("Es ist ein Fehler aufgetreten.")
finally:
    print("Ich werde in jedem Fall ausgeführt")
    
    
try:
    f = open("text.txt", "w")
    f.write("Hallo Welt")
except Exception:
    pass
finally:
    f.close()
    
    
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(10 / zahl)
except ValueError:
    print("Bitte gib eine ganze Zahl ein.")
except ZeroDivisionError:
    print("Division durch Null ist nicht erlaubt.")