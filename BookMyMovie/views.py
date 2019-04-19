from django.shortcuts import render
from django.http import HttpResponse
import requests
from BookMyMovie.models import Movie, ShowDay,Theatre, ShowTime
# Create your views here.


def index(request):
    movies = Movie.objects.all()

    return render(request,'BookMyMovie/BookMovie.html',{'movies':movies})

def handler404(request, exception):
    data = {"name": "You entered something wrong here"}
    return render(request,'BookMyMovie/404.html', data)

def handler500(request, exception):
    data = {"name": "There is some error"}
    return render(request,'BookMyMovie/500.html', data)

def movie(request,m):

    movie = Movie.objects.get(id=m)
    showdays = ShowDay.objects.all()
    data = {'movie':movie,'showdays':showdays}
    return render(request,'BookMyMovie/BMmovie.html',data)

def theatre(request,m,day):
    
    theatres = Theatre.objects.all()
    shows = {}
    for th in theatres:
        # print(th.name)
        show_list = ShowTime.objects.filter(movieID=m).filter(day=day).filter(TheatreID=th.id)
        shows[th.name] = show_list

    # print(shows)

    data = {'movieID':m,'day':day,'theatres':theatres}

    return render(request,'BookMyMovie/theatre.html',data)
