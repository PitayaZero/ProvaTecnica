from hashlib import blake2b
from pyclbr import Class
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    imagem = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"