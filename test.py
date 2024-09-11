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

mehrzeiliger_text = """
Dies ist ein Beispiel für einen mehrzeiligen String in Python.
Du kannst hier beliebig viele Zeilen schreiben.
Sogar mit Zeilenumbrüchen!
"""

print(mehrzeiliger_text)