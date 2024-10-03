import numpy as np
import matplotlib.pyplot as plt

# Signal erzeugen und Fourier-Transformieren
t = np.linspace(0, 1, 1024)
x = np.sin(2*np.pi*50*t) + np.cos(2*np.pi*120*t)
X = np.fft.fft(x)

# Plotten
plt.plot(np.abs(X))
plt.show()