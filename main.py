class Pokemon:
    
    def __init__(self, n, level):
        self.n = n
        self.__level = level
        self.vorstellen()
        
    def vorstellen(self):
        print(f"{self.n}, {self.n}!")
        
    def get_level(self):
        return self.__level
        
if __name__ == "__main__":
    bisasam = Pokemon("Bisasam", 0) # Bisasam, Bisasam!