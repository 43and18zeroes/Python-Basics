import pandas as pd
import numpy as np

def portfolio_return(returns):
  """Berechnet die durchschnittliche Rendite eines Portfolios."""
  return np.mean(returns)