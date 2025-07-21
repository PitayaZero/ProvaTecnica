from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Usuario, Evento, InscricaoEvento
from .serializers import UsuarioSerializer, EventoSerializer, InscricaoEventoSerializer



@api_view(['GET'])
def listar_users(request):
    users = User.objects.all()
    data = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        for user in users
    ]
    return Response(data)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() # type: ignore
    serializer_class = UsuarioSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all() # type: ignore
    serializer_class = EventoSerializer

    def perform_create(self, serializer):
        # Pega o usuário autenticado
        user = self.request.user
        
        # Preenche automaticamente os campos
        serializer.save(
            idUsuarioCriador=str(user.id),
            nomeUsuario=f"{user.first_name} {user.last_name}".strip() or user.username
        )

@api_view(['POST'])
def inscrever_evento(request, evento_id):
    """Inscreve o usuário autenticado em um evento"""
    try:
        evento = Evento.objects.get(id=evento_id)
        usuario = request.user
        
        # Verifica se já está inscrito
        if InscricaoEvento.objects.filter(evento=evento, usuario=usuario).exists():
            return Response({
                'error': 'Você já está inscrito neste evento'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Cria a inscrição
        inscricao = InscricaoEvento.objects.create(evento=evento, usuario=usuario)
        serializer = InscricaoEventoSerializer(inscricao)
        
        return Response({
            'message': 'Inscrição realizada com sucesso!',
            'inscricao': serializer.data
        }, status=status.HTTP_201_CREATED)
        
    except Evento.DoesNotExist:
        return Response({
            'error': 'Evento não encontrado'
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def cancelar_inscricao(request, evento_id):
    """Cancela a inscrição do usuário autenticado em um evento"""
    try:
        evento = Evento.objects.get(id=evento_id)
        usuario = request.user
        
        inscricao = InscricaoEvento.objects.get(evento=evento, usuario=usuario)
        inscricao.delete()
        
        return Response({
            'message': 'Inscrição cancelada com sucesso!'
        }, status=status.HTTP_200_OK)
        
    except Evento.DoesNotExist:
        return Response({
            'error': 'Evento não encontrado'
        }, status=status.HTTP_404_NOT_FOUND)
    except InscricaoEvento.DoesNotExist:
        return Response({
            'error': 'Você não está inscrito neste evento'
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def listar_inscritos_evento(request, evento_id):
    """Lista todos os usuários inscritos em um evento específico"""
    try:
        evento = Evento.objects.get(id=evento_id)
        inscricoes = InscricaoEvento.objects.filter(evento=evento)
        serializer = InscricaoEventoSerializer(inscricoes, many=True)
        
        return Response({
            'evento': evento.titulo,
            'total_inscritos': inscricoes.count(),
            'inscritos': serializer.data
        })
        
    except Evento.DoesNotExist:
        return Response({
            'error': 'Evento não encontrado'
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def meus_eventos_inscritos(request):
    """Lista todos os eventos em que o usuário autenticado está inscrito"""
    usuario = request.user
    inscricoes = InscricaoEvento.objects.filter(usuario=usuario)
    serializer = InscricaoEventoSerializer(inscricoes, many=True)
    
    return Response({
        'total_eventos': inscricoes.count(),
        'eventos': serializer.data
    })