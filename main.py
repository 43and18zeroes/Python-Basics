from scipy import stats

# Zufallszahlen erzeugen
data = stats.norm.rvs(size=1000, loc=5, scale=2)

# Mittelwert und Standardabweichung berechnen
mean = np.mean(data)
std = np.std(data)
print(mean, std)