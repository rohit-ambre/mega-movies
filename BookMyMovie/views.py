from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def landing(request):
    return HttpResponse("This is a landing page")

def index(request):
    return HttpResponse("Home page for BookMyMovie")