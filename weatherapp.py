import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = open('API.txt','r').readline()

print(type(API_KEY))
CITY = 'TOKYO'

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)