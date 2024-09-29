import numpy as np
from scipy.fft import fft

# Create a sample signal
time = np.linspace(0, 1, 500)
frequency = 5  # Hz
signal = np.sin(2 * np.pi * frequency * time)

# Compute Fourier Transform
fft_result = fft(signal)
