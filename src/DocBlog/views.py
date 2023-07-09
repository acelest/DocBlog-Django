from django.http import HttpResponse
from django.shortcuts import render


# 👀 Créer une vue pour l'URL
# def index(request):
#     return HttpResponse("Bienvenue sur mon site")


# 🔖 Retourner un template

def index(request):
    return render(request,"index.html")