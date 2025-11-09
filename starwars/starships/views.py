from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

# Create your views here.
def send_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None

def update_data(data):
    films = data['films']
    pilots = data['pilots']
    # starships = data['starships']

    new_films = list()
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])

    new_pilots = []
    for pilot_url in pilots:
        pilot_data = send_req(pilot_url)
        if pilot_data:
            new_pilots.append(pilot_data.get('name', 'Unknown Pilot'))

    # new_starships = list()
    # for starship in starships:
    #     starship = send_req(starship)
    #     new_starships.append(starship['name'])

    data['films'] = new_films
    data['pilots'] = new_pilots
    # data['starships'] = new_starships

    return data

def get_xwing_info(request):
    data = send_req('https://swapi.dev/api/starships/12/')
    if data:
        updated_data = update_data(data)

        return render(request, 'starships/starship.html', updated_data)
    return HttpResponse('не удалось')

def get_imperial_shuttle_info(request):
    data = send_req('https://swapi.dev/api/starships/22/')
    if data:
        updated_data = update_data(data)

        return render(request, 'starships/starship.html', updated_data)
    return HttpResponse('не удалось')

def get_death_star_info(request):
    data = send_req('https://swapi.dev/api/starships/9/')
    if data:
        updated_data = update_data(data)

        return render(request, 'starships/starship.html', updated_data)
    return HttpResponse('не удалось')