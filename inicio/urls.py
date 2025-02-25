from inicio.views import inicio, cargar_articulo, lista_de_productos
from django.urls import path


urlpatterns = [
    path("",inicio,name="inicio"),
    path("cargar-articulo/", cargar_articulo, name="cargar_articulo"),
    path("lista-de-productos/", lista_de_productos, name="lista_de_productos")
]