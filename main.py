import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Ersetze durch deinen eigenen API-Schlüssel
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(f"Das Wetter in {city} ist: {data['weather'][0]['description']}")

city = input("Gib eine Stadt ein: ")
get_weather(city)