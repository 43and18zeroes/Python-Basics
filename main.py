class MeineKlasse:
    def __init__(self, x):
        if x <= 0:
            raise ValueError("Wert muss größer als Null sein.")
        self.x = x

try:
    objekt = MeineKlasse(-2)
except ValueError as e:
    print(e)