from django.db import models
from django.utils import timezone

class Coach(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    frase = models.TextField()
    inspirador = models.CharField(max_length=255, null=True)
    criado_em =  models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__ (self):
        return self.nome

def Users(models.Model):
    nome = models.ForeignKey(Coach, on delete = none)
    emial = models.EmailField(max_length=225, verbose_name='Email')
    senha = models.CharField(max_length=16, verbose_name='Senha')