import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

start = datetime(2023, 1, 1)
end = datetime(2024, 1, 1)
print(random_date(start, end))  # Zufälliges Datum im Jahr 2023
