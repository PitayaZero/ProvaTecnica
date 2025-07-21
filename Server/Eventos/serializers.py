from pydoc import classname
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario, Evento, InscricaoEvento

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'email', 'imagem', 'data_criacao']


class EventoSerializer(serializers.ModelSerializer):
    idUsuarioCriador = serializers.CharField(read_only=True)
    nomeUsuario = serializers.CharField(read_only=True)
    
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descricao', 'idUsuarioCriador', 'nomeUsuario', 'imagem', 'data_criacao']


class InscricaoEventoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)
    evento_titulo = serializers.CharField(source='evento.titulo', read_only=True)
    
    class Meta:
        model = InscricaoEvento
        fields = ['id', 'evento', 'usuario', 'usuario_nome', 'evento_titulo', 'data_inscricao']
        read_only_fields = ['usuario', 'data_inscricao']