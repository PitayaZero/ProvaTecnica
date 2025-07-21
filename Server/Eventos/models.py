from hashlib import blake2b
from pyclbr import Class
from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    imagem = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"



class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    idUsuarioCriador = models.CharField(max_length=100)
    nomeUsuario = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} {self.nomeUsuario}"


class InscricaoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscricoes_eventos')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['evento', 'usuario']  # Evita inscrições duplicadas

    def __str__(self):
        return f"{self.usuario.username} - {self.evento.titulo}"