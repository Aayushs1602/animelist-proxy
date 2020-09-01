from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')

def v1(request):
    if request.method == "POST":
        name = request.POST.get('search')
        while True:
            try:
                json_file = requests.get(f"https://api.jikan.moe/v3/search/anime?q={name}&page=1").json()

                with open('static/anime.json', 'w') as f:
                    json.dump(json_file["results"], f)
                break
            except:
                pass
        return render(request, "searched.html")

    return HttpResponse("<img src='https://lh3.googleusercontent.com/pw/ACtC-3cCAnIragkIIy7_qEkD1rSAyUa9R4pFJ4EaHIx2GYjysgRiaaLAUl-JJX15-ZmVcVHFfGg8FeZjzPKsJcuJO5VPCAH4k91B6jyF5gbSj1H31OlRDDXxM9A24FKPDBILdPw1N06o5iq3i9w65aKgIOpV=w1509-h938-no?authuser=0' style='width:62%; height: auto;'/>")
    
