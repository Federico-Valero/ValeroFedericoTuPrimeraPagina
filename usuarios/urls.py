from django.urls import path
from usuarios.views import login, registro, editar_perfil, datos_usuario, CambioPassworld
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("registro/", registro, name="registro"),
    path("editar-perfil/", editar_perfil, name="editar_perfil"),
    path("datos_usuario/", datos_usuario, name="datos_usuario"),
    path("editar-perfil/cambio_pass", CambioPassworld.as_view(), name="cambio_pass"),
]
