from django.urls import path

from .views import registrar, entrar, sair, validarUsuario

app_name = "contas"
urlpatterns = [
    path("registrar/", registrar, name="registrar"),
    path("entrar/", entrar, name="entrar"),
    path("sair/", sair, name="sair"),
    path("validar/", validarUsuario, name="validar")
]