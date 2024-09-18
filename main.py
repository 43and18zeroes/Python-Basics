class Pokemon:
    
    def __init__(self, name):
        self.__n = name
        self.__lebenspunkt = 42
        self.__level = 1
        
    def vorstellen(self):
        print(f"{self.__n}, {self.__n}!")
        
    def zeige_lebenspunkt(self):
        return self.__lebenspunkt
    
    def zeige_level(self):
        return self.__level
                
if __name__ == "__main__":
    p1 = Pokemon("Pikachu")
    p1 = Pokemon("Bisasam")
    
    print(p1.zeige_level()) # 1