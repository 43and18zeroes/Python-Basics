import random
population = ['rot', 'blau', 'grün']
weights = [0.7, 0.2, 0.1]  # Rot wird häufiger ausgewählt
zufalls_farbe = random.choices(population, weights=weights)[0]
print(zufalls_farbe)