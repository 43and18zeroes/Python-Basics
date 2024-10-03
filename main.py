from scipy.optimize import minimize

# Funktion minimieren
def f(x):
    return x**2 + 2*x + 1

result = minimize(f, x0=2)
print(result.x)