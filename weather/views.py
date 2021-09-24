import requests
from django.shortcuts import render
from . models import City
from .forms import CityForm

def index(request):

    appid = '2cc2e81d07f3347a238059f078af497d'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method =='POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
#Записую в змінну потрібні поля
        city_info = {
            'city': city.name,
            'temp': res["main"] ["temp"],
            'temp_min': res["main"] ["temp_min"],
            'temp_max': res["main"] ["temp_max"],
            'icon': res["weather"] [0] ["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'index.html', context)