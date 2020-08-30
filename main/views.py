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

    return HttpResponse("<h1>PAGE NOT FOUND 404</h1>")
    