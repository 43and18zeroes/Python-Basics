print(bool(0.1)) # True
print(bool(-0.1)) # True
print(bool("")) # False

print(int("1.5"))

print(int(float("1.5")))

int(42.5) # 42
float(-1) # -1.0
str(0.5) # "0.5"
bool(0.001) # True
str("False") # 'False'
int(False) # 0
float("10") # 10.0
bool('0') # False
int("False") # Fehlermeldung weil String zu Int
float("True") # Fehlermeldung weil String zu Float

def quadrat(zahl):
    """Berechnet das Quadrat einer Zahl.

    Args:
        zahl: Die Zahl, deren Quadrat berechnet werden soll.

    Returns:
        Das Quadrat der gegebenen Zahl.
    """

    return zahl * zahl

# Aufruf der Funktion und Ausgabe des Ergebnisses
ergebnis = quadrat(5)
print(ergebnis)  # Ausgabe: 25