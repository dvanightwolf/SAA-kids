from django.shortcuts import render
from .game import ScratchGame
import requests


def api(request):
    games = None
    url = requests.get('https://api.scratch.mit.edu/users/MoonKnightShark/projects').json()
    result_list = []
    for json_dect in url:
        result_list.append(ScratchGame(json_dect['id'], json_dect['title'], json_dect['image']))
    return render(request, 'games.html', {'result_list': result_list})


def play_game(request, id, title):
    return render(request, 'play_game.html', {'id': id, 'title': title})
