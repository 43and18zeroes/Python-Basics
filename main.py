try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(10 / zahl)
except ValueError:
    print("Bitte gib eine ganze Zahl ein.")
except ZeroDivisionError:
    print("Division durch Null ist nicht erlaubt.")