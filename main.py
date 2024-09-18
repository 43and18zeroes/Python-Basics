class Pokemon:
    
    def __init__(self, n, level):
        self.n = n
        self.level = level
        
    def vorstellen(self):
        print(f"{self.n}, {self.n}!")
        
if __name__ == "__main__":
    bisasam = Pokemon("Bisasam", 0)
    bisasam.vorstellen() # Bisasam, Bisasam!