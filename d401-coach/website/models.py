from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    # nome = models.ForeignKey(Coach, on_delete = None)
    email = models.EmailField(max_length=225, verbose_name='Email', unique=True)
    senha = models.CharField(max_length=16, verbose_name='Senha')

    def __str__ (self):
        return self.email

class Coach(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    frase = models.TextField()
    inspirador = models.CharField(max_length=255, null=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    criado_em =  models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__ (self):
        return self.nome

    