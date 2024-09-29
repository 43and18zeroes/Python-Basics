import numpy as np

# Define a simple quadratic function
def f(x):
    return x**2

# Derivative of f(x)
def df(x):
    return 2*x

# Gradient Descent Algorithm
def gradient_descent(start, learning_rate, n_iter):
    x = start
    for _ in range(n_iter):
        gradient = df(x)
        x = x - learning_rate * gradient
    return x

# Initial value and parameters
x0 = 10
learning_rate = 0.1
n_iter = 100

# Run gradient descent
min_value = gradient_descent(x0, learning_rate, n_iter)
