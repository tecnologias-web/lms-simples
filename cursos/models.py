from django.db import models

class Curso(models.Model):

    nome = models.CharField(max_length=120)
    sigla = models.CharField(max_length=5, blank=True)
    duracao = models.SmallIntegerField()
    descricao = models.TextField()

class Disciplina(models.Model):

    nome = models.CharField(max_length=150)
    carga_horaria = models.IntegerField()

    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)