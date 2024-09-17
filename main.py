from taschenrechner import *

summe = addieren(1, 2)

print(summe)

print(__name__) # __main__

def begruessung():
    print("Hallo aus dem Modul!")

if __name__ == "__main__":
    print("Das Skript wird direkt ausgeführt.")
    begruessung()
