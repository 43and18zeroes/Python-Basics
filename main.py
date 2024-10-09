import pandas_datareader as web

def get_stock_data(ticker, start, end):
  """Lädt historische Kursdaten für einen bestimmten Wertpapier."""
  df = web.DataReader(ticker, 'yahoo', start, end)
  return df