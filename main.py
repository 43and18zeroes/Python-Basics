try:
    liste = [1, 2, 3]
    element = liste[3]
except IndexError:
    print("Index außerhalb des Bereichs.")
else:
    print("Element gefunden:", element)