import sympy as sp

# Gleichungssystem definieren
x, y = sp.symbols('x y')
eq1 = x + 2*y - 4
eq2 = 3*x - y - 3

# Gleichungssystem lösen
sol = sp.solve([eq1, eq2], [x, y])
print(sol)