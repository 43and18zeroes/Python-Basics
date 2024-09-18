class Hund:
    def __init__(self, farbe, rasse, name):
        self.farbe = farbe
        self.rasse = rasse
        self.name = name
        
    def vorstellen(self):
        print(self.name)
        
    def essen(self):
        pass
    
    def bellen(self):
        pass
    
    def laufen(self):
        pass
    
dog1 = Hund('Braun', 'Schäferhund', 'Fritzi')
dog2 = Hund('Schwarz', 'Schäferhund', 'Wuffi')

dog1.vorstellen() # Fritzi
dog2.vorstellen() # Wuffi