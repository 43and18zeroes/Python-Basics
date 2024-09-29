import numpy as np
from scipy.integrate import simps

# Define a function to integrate
def f(x):
    return np.sin(x)

x = np.linspace(0, np.pi, 100)
y = f(x)

# Compute the integral using Simpson's rule
result = simps(y, x)
