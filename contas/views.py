from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .models import Usuario

def registrar(request):
    context = {}
    if request.POST:
        email  = request.POST.get("email")
        nome_completo  = request.POST.get("nome")
        nascimento  = request.POST.get("nascimento")
        senha  = request.POST.get("password")
        senha2  = request.POST.get("password2")
        if senha == senha2:
            usuario = Usuario(email=email, nome_completo=nome_completo, nascimento=nascimento)
            usuario.set_password(senha)
            usuario.save()
            login(request, usuario)
            return redirect("home")
    else:
        return render(request, "registrar.html", context)

def entrar(request):
    context = {}
    if request.POST:
        email = request.POST.get("email")
        senha = request.POST.get("password")
        usuario = authenticate(username=email, password=senha)
        login(request, usuario)
        return redirect("home")
    return render(request, "entrar.html", context)
    
def sair(request):
    logout(request)
    return redirect("home")

def validarUsuario(request):
    email = request.GET.get("email")
    data = {
        "existe":Usuario.objects.filter(email=email).exists()
    }
    return JsonResponse(data)
