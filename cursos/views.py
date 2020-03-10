from django.shortcuts import render

from .models import Curso

# Create your views here.
def cursos(request):
    context = {
        "cursos":Curso.objects.all()
    }
    return render(request, "cursos.html", context)

def curso(request, sigla):
    curso = Curso.objects.get(sigla=sigla)
    context = {
        "curso":curso
    }
    return render(request, "curso.html", context)