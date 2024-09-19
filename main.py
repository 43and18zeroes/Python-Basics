liste = [1, 2, 3, "Flo", "Junus", "Manu"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    print(liste[index])
except Exception:
    print("Es ist ein Fehler aufgetreten.")