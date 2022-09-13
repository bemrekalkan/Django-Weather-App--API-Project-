from django.shortcuts import render
from decouple import config
import requests

def index(request):
    API_KEY = config("API_KEY")
    city = "Eskisehir"
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    print(response) #! 👉 <Response [200]>
    return render(request, 'weatherapp/index.html')