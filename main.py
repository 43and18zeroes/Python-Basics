import sympy as sp

# Symbolische Variablen definieren
x = sp.Symbol('x')

# Ableitung berechnen
f = sp.sin(x)
df = sp.diff(f, x)
print(df)

# Integral berechnen
integral = sp.integrate(f, x)
print(integral)