from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager

class Usuario(AbstractBaseUser):

    email = models.EmailField(unique=True)

    nome_completo = models.CharField(max_length=155)

    nascimento = models.DateField()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["nome_completo", "nascimento"]

    objects = UserManager()
