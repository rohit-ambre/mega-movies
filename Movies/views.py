from django.shortcuts import render, redirect
import requests
# Create your views here.

def landing(request):
    url = 'http://www.omdbapi.com/?apikey=******&r=json&s={}'
    
    if request.method == 'POST':
        term = request.POST.get("search", "")+'*' # added * for wildcard search
        res = requests.get(url.format(term))
        data = {'movies':res.json()}
    else:
        term = 'Thor'
        res = requests.get(url.format(term))
        data = {'movies':res.json()}
    return render(request,'Movies/landing.html',data)

def testredirect(request):
    return redirect('/Movies')

def display(request, imdb):
    url = 'http://www.omdbapi.com/?apikey=******&r=json&i={}'
    
    if imdb:
        res = requests.get(url.format(imdb))
        data = {'movie':res.json()}


    return render(request,'Movies/display-movie.html',data)