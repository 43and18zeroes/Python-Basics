class Mammal:
    def __init__(self, farbe, rasse, name):
        self.farbe = farbe
        self.rasse = rasse
        self.name = name
        
    def vorstellen(self):
        print(self.name)
        
    def essen(self):
        pass
    
    def laufen(self):
        pass

class Hund(Mammal):
    def bellen(self):
        pass
    
class Katze(Mammal):
    def miauen(self):
        print("Miau")

    
dog1 = Hund('Braun', 'Schäferhund', 'Fritzi')
dog2 = Hund('Schwarz', 'Schäferhund', 'Wuffi')

dog1.vorstellen() # Fritzi
dog2.vorstellen() # Wuffi