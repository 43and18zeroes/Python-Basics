class Pokemon:
    
    def __init__(self, name):
        self.__n = name
        self.__lebenspunkte = 42
        self.__level = 1
        
    def vorstellen(self):
        print(f"{self.__n}, {self.__n}!")
        
    def zeige_lebenspunkte(self):
        return self.__lebenspunkte
    
    def zeige_level(self):
        print(f"{self.__n} :: {self.__level}")
    
    def entwickeln(self):
        self.__level += 1
        
    def attackieren(self, other, schaden):
        other.__lebenspunkte -= schaden
        
                
if __name__ == "__main__":
    p1 = Pokemon("Pikachu")
    p2 = Pokemon("Bisasam")
    
    p1.attackieren(p2, 10)
    print(p2.zeige_lebenspunkte()) # 32