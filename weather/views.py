from django.shortcuts import render
from weather.parse import get_forecast_weather

def index(request):
    return render(request, 'weather/index.html')

def post(request):
    try:
        city = request.POST['city']
    except:
        pass
    return render(request, 'weather/result.html', {'lst' : get_forecast_weather(city), 'city' : city.capitalize()})
