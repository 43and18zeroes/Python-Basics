from scipy.integrate import quad

# Funktion integrieren
def f(x):
    return x**2 * np.exp(-x)

result, error = quad(f, 0, np.inf)
print(result)