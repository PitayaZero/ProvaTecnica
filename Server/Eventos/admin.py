from django.contrib import admin
from .models import Usuario, Evento, InscricaoEvento

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['nome', 'sobrenome', 'email']
    readonly_fields = ['data_criacao']
    ordering = ['-data_criacao']

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nomeUsuario', 'idUsuarioCriador', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'descricao', 'nomeUsuario']
    readonly_fields = ['data_criacao']
    ordering = ['-data_criacao']

@admin.register(InscricaoEvento)
class InscricaoEventoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'evento', 'data_inscricao']
    list_filter = ['data_inscricao', 'evento']
    search_fields = ['usuario__username', 'evento__titulo']
    readonly_fields = ['data_inscricao']
    ordering = ['-data_inscricao']
