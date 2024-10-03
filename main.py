from scipy.integrate import solve_ivp

# Einfache Differentialgleichung lösen
def f(t, y):
    return -y

sol = solve_ivp(f, [0, 10], [1])
print(sol.t, sol.y[0])