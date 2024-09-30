import numpy as np
from scipy.optimize import newton

# Define the function and its derivative
def f(x):
    return np.cos(x) - x

# Use Newton-Raphson method to find the root
root = newton(f, x0=0.5)
