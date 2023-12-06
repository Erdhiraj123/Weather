from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'patna'

    # OpenWeatherMap API
    weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b0d85f0cd81af373d3a89c274d795423'
    openweathermap_url = weather_api_url.format(city)
    # print(openweathermap_url)
    
    # Google Custom Search API
    search_api_url = 'https://www.googleapis.com/customsearch/v1?key=b0d85f0cd81af373d3a89c274d795423&cx=b686584adf1c64586&q={}&start=1&searchType=image&imgSize=xlarge'
    google_search_url = search_api_url.format(city + " 1920x1080")
    # print(google_search_url)

    try:
        # Get data from OpenWeatherMap API
        openweathermap_data = requests.get(openweathermap_url, params={'units': 'metric'}).json()
        description = openweathermap_data['weather'][0]['description']
        icon = openweathermap_data['weather'][0]['icon']
        temp = openweathermap_data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
       
        })

    except KeyError as e:
        exception_occurred = True
        messages.error(request, f'KeyError: {e}. Please check the data returned by the APIs.')
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_occurred': exception_occurred,
          
        })


