from bs4 import BeautifulSoup
import requests

def scrape_website(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  
  # Beispiel: Alle Überschriften extrahieren
  headings = soup.find_all('h2')
  for heading in headings:
    print(heading.text)

# Beispiel-URL
url = "https://www.example.com"
scrape_website(url)