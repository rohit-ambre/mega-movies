from django.shortcuts import render
from django.http import HttpResponse
import requests
from BookMyMovie.models import Movie, ShowDay,Theatre, ShowTime, Booking


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
    combined_dict = {}

    for th in theatres:
        show_list = ShowTime.objects.filter(movieID=m).filter(day=day).filter(TheatreID=th.id)
        shows[th.name] = show_list
        combined_dict[th.name] = [th,show_list]

    data = {'movieID':m,'day':day,'theatres':theatres,'shows':shows,'combined_dict':combined_dict}

    return render(request,'BookMyMovie/theatre.html',data)


def seat(request,m,day,show):

    if request.method == 'POST':
        print(request.POST)
    
    show_data = ShowTime.objects.get(id=show)
    theatre_data = Theatre.objects.get(name=show_data.TheatreID)
    bookings = Booking.objects.filter(show=show)

    booked_seats_nested = []
    booked_seats = []
    for booking in bookings:
        booked_seats_nested.append(booking.seats.split(','))
    
    def removeNestings(l): 
        for i in l: 
            if type(i) == list: 
                removeNestings(i) 
            else: 
                booked_seats.append(int(i))

    removeNestings(booked_seats_nested)

    seats_arr = [i for i in range(1,theatre_data.seats+1)]

    seat_details = {}
    for s in seats_arr:
        if s in booked_seats:
            seat_details[s] = [s,'active','disabled']
        else:
            seat_details[s] = [s,'','']    

    data = {'show_data':show_data,'seats_arr': seats_arr,'booked_seats':booked_seats,'seat_details':seat_details}

    return render(request,'BookMyMovie/seat.html',data)