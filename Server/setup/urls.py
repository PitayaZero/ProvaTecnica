
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from Eventos.views import listar_users, UsuarioViewSet, EventoViewSet, inscrever_evento, cancelar_inscricao, listar_inscritos_evento, meus_eventos_inscritos

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'evento', EventoViewSet, basename='evento')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticar/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns += router.urls

urlpatterns += [
    path('ListarUsuarios/', listar_users, name='listar_users'),
    path('evento/<int:evento_id>/inscrever/', inscrever_evento, name='inscrever_evento'),
    path('evento/<int:evento_id>/cancelar-inscricao/', cancelar_inscricao, name='cancelar_inscricao'),
    path('evento/<int:evento_id>/inscritos/', listar_inscritos_evento, name='listar_inscritos_evento'),
    path('meus-eventos-inscritos/', meus_eventos_inscritos, name='meus_eventos_inscritos'),
]
