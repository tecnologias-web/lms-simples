from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def premios(request):
    context = {
        "titulo":"Prêmios recebidos pela Impacta"
    }
    return render(request, "premios.html", context)

def olaMundo(request):
    return HttpResponse("<h1>Olá Mundo!</h1>")