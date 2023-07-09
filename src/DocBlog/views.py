from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# 👀 Créer une vue pour l'URL
# def index(request):
#     return HttpResponse("Bienvenue sur mon site")


# 🔖 Retourner un template

# def index(request):
#     return render(request,"index.html")

def index(request):
    # creation du dictionnaire context={}
    date=datetime.today()
    # print(date)
    # print(type(date))
    return render(request, "index.html", context={"prenom": "aubin","date":date})

