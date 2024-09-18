# class Pokemon:
    
#     def __init__(self, name):
#         self.__n = name
#         self.__lebenspunkte = 42
#         self.__level = 1
        
#     # Magische Methode
#     def __str__(self):
#         return f"Name: {self.__n}\nLebenspunkte: {self.__lebenspunkte}\nLevel: {self.__level}"
    
#     def __gt__(self, other):
#         return self.__level > other.__level
        
#     def vorstellen(self):
#         print(f"{self.__n}, {self.__n}!")
        
#     def zeige_lebenspunkte(self):
#         return self.__lebenspunkte
    
#     def zeige_level(self):
#         print(f"{self.__n} :: {self.__level}")
    
#     def entwickeln(self):
#         self.__level += 1
        
#     def attackieren(self, other, schaden):
#         other.__lebenspunkte -= schaden
        
                
# if __name__ == "__main__":
#     p1 = Pokemon("Pikachu")
#     p2 = Pokemon("Bisasam")
    
#     p1.entwickeln()
    
#     print(p1 > p2) # True
    
#     str(p1)
    
class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.lebenspunkte = 42
        self.level = 1
        
    def vorstellen(self): # Methoden Definition
        print(f"{self.name}, {self.name}!")
        
bisasam = Pokemon("Bisasam")
bisasam.vorstellen() # Methoden Aufruf

len("asldkfjlsdkjflikds")
len([1, 2, 3])