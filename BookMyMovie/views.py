from django.shortcuts import render
from django.http import HttpResponse
import requests
from BookMyMovie.models import Movie
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