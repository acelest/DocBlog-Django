from django.http import HttpResponse


# 👀 Créer une vue pour l'URL
def index(request):
    return HttpResponse("Bienvenue sur mon site")


