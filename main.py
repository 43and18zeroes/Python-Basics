class MeineException(Exception):
    pass

def meine_funktion(x):
    if x < 0:
        raise MeineException("Zahl muss positiv sein.")

try:
    meine_funktion(-5)
except MeineException as e:
    print(e)