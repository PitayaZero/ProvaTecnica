
from django.contrib import admin
from django.urls import path
from Eventos.views import registrarUsuario
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from Eventos.views import listar_users
from Eventos.views import UsuarioViewSet

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/', registrarUsuario, name='registrarUsuario'),
    path('autenticar/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns += router.urls

urlpatterns += [
    path('ListarUsuarios/', listar_users, name='listar_users'),
]
