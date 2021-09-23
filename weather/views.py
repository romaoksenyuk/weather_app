import requests
from django.shortcuts import render

def index(request):

#Просто ключ для url
    appid = '2cc2e81d07f3347a238059f078af497d'

#Ссилка на сайт з якого буде батись інфа про погоду
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Lutsk'

#Змінна в яку заносяться дані в форматі json та перетворються в список
    res = requests.get(url.format(city)).json()

#Записую в змінну потрібні поля
    city_info = {
        'city': city,
        'temp': res["main"] ["temp"],
        'temp_min': res["main"] ["temp_min"],
        'temp_max': res["main"] ["temp_max"],
        'icon': res["weather"] [0] ["icon"]
    }
    context = {'info': city_info}

    return render(request, 'index.html', context)