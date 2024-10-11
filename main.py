import numpy as np

def volatility(returns):
  """Berechnet die Volatilität (Standardabweichung) einer Rendite."""
  return np.std(returns)