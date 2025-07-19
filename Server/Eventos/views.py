from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def registrarUsuario(request):

    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not username or not email or not password:
        return Response({
            'error': 'Todos os campos são obrigatórios (username, email, password)'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verifica se o usuário já existe
    if User.objects.filter(username=username).exists():
        return Response({
            'error': 'Nome de usuário já existe'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(email=email).exists():
        return Response({
            'error': 'Email já está em uso'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Cria o novo usuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return Response({
            'message': 'Usuário criado com sucesso',
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'error': f'Erro ao criar usuário: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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

