from scipy.integrate import odeint
import numpy as np

# Define the ODE: dy/dt = -2y
def model(y, t):
    dydt = -2 * y
    return dydt

y0 = 1  # Initial condition
t = np.linspace(0, 5, 100)  # Time points

# Solve ODE
y = odeint(model, y0, t)
