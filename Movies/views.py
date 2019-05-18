from django.shortcuts import render, redirect
import requests
from django.conf import settings
# Create your views here.

def landing(request):
    url = 'http://www.omdbapi.com/?apikey={0}&r=json&s={1}'

    if request.method == 'POST':
        term = request.POST.get("search", "")+'*' # added * for wildcard search
        res = requests.get(url.format(settings.API_KEY,term))
        data = {'movies':res.json()}
    else:
        term = 'Thor'
        res = requests.get(url.format(settings.API_KEY,term))
        data = {'movies':res.json()}
    return render(request,'Movies/landing.html',data)

def moviesredirect(request):
    return redirect('/Movies')

def display(request, imdb):
    url = 'http://www.omdbapi.com/?apikey={0}&r=json&i={1}'
    
    if imdb:
        res = requests.get(url.format(settings.API_KEY,imdb))
        data = {'movie':res.json()}


    return render(request,'Movies/display-movie.html',data)