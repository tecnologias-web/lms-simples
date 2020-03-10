from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def olaMundo(request):
    return HttpResponse("<h1>Olá Mundo!</h1>")