from scipy.interpolate import interp1d

# Datenpunkte erzeugen
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Interpolation durchführen
f = interp1d(x, y)
x_new = np.linspace(0, 10, 100)
y_new = f(x_new)

# Plotten
plt.plot(x, y, 'o', x_new, y_new, '-')
plt.show()