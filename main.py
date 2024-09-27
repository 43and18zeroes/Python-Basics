import matplotlib.pyplot as plt
import numpy as np

# Erstellen von Zufallsdaten
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Erstellen eines Liniendiagramms
plt.plot(x, y)
plt.xlabel('x-Achse')
plt.ylabel('y-Achse')
plt.title('Sinuskurve')
plt.grid(True)
plt.show()