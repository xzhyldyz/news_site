import requests
from django.conf import settings

def get_weather():
    api_key = 'f95630be539467d0ddc867eece454246'
    city = 'Bishkek'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    try:
        response = requests.get(url)
        data = response.json()

        return {
            'city': city,
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    except:
        return None

