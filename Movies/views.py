from django.shortcuts import render
import requests
# Create your views here.

def landing(request):
    url = 'http://www.omdbapi.com/?apikey=*****&r=json&s={}'
    
    if request.method == 'POST':
        term = request.POST.get("search", "")
        res = requests.get(url.format(term))
        data = {'movies':res.json()}
        # print(res.text)
        # return render(request,'Movies/landing.html',data)
    else:
        term = 'Thor'
        res = requests.get(url.format(term))
        data = {'movies':res.json()}
    return render(request,'Movies/landing.html',data)