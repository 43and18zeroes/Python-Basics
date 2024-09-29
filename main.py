import numpy as np

# Define the system of equations as matrices
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solve the system Ax = b
x = np.linalg.solve(A, b)
