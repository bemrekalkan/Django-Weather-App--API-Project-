from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

def index(request):
    API_KEY = config("API_KEY")
    city = "Ankara"
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    print(response) #! 👉 <Response [200]>
    pprint(content)

    return render(request, 'weatherapp/index.html')