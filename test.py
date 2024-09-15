print(()) # (), leeres Tupel

test_tupel = (1, 2, 3)
print(test_tupel[1]) # 2
print(test_tupel[-2]) # 2
print(test_tupel[-3]) # 1


def addieren(a, b):
    summe = a + b
    return a, b, summe

ergebnis = addieren(1, 4)
print(ergebnis) # (1, 4, 5), ein Tupel
print(type(ergebnis)) # <class 'tuple'>


def addieren2(a, b):
    summe = a + b
    return summe

ergebnis = addieren2(1, 4)
print(ergebnis) # 5, ein Integer
print(type(ergebnis)) # <class 'int'>

def addieren3(*summanden):
    print(type(summanden)) # <class 'tuple'>
    
addieren3()