from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Verbindung zur Datenbank herstellen
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Beispiel: Abfrage von Daten
users = session.query(User).all()
for user in users:
  print(user.name, user.email)