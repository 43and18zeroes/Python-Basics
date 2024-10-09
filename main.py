import talib

def calculate_rsi(prices, period=14):
  """Berechnet den Relative Strength Index (RSI)."""
  rsi = talib.RSI(prices, timeperiod=period)
  return rsi