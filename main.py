import requests
import os

api_key = os.getenv("INPUT_OPEN_WEATHER_KEY")

city = 'Paris'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = round(data['main']['temp'] - 273.15, 2)
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} Celsius')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
