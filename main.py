liste = [1, 2, 3, "Flo", "Junus", "Manu"]

try:
    index = int(input("Bitte gib einen Index ein: "))
    print(liste[index])
except IndexError as ex:
    print(f"Der Zugriff ist fehlgeschlagen.\n{ex}")