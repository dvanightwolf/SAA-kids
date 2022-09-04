from django.shortcuts import render, HttpResponse
from .game import ScratchGame
import requests


def api(request):
    try:
        games = None
        url = requests.get('https://api.scratch.mit.edu/users/MoonKnightShark/projects').json()
        result_list = []
        index = 0
        for json_dect in url:
            index = index+1
            result_list.append(ScratchGame(index,json_dect['id'], json_dect['title'], json_dect['image'],
                                           json_dect['description']))

        return render(request, 'games.html', {'result_list': result_list})
    except:
        return render(request, 'error.html')


def play_game(request, id, title):
    return render(request, 'play_game.html', {'id': id, 'title': title})


def solar(request):
    return render(request, 'stars.html')
