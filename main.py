def simple_interest(principal, rate, time):
  """Berechnet einfache Zinsen."""
  return principal * rate * time

def compound_interest(principal, rate, time, n=12):
  """Berechnet Zinseszinsen."""
  amount = principal * (pow((1 + rate/n), n*time))
  CI = amount - principal
  return CI