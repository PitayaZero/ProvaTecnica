from pydoc import classname
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'email', 'imagem', 'data_criacao']
