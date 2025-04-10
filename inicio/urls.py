from inicio.views import inicio, cargar_articulo, lista_de_productos, ver_articulo, ModificarArticulo, EliminarArticulo, cambio_imagen, about
from django.urls import path


urlpatterns = [
    path("",inicio,name="inicio"),
    path("cargar-articulo/", cargar_articulo, name="cargar_articulo"),
    path("lista-de-productos/", lista_de_productos, name="lista_de_productos"),
    path("modificar-articulo/<int:pk>", ModificarArticulo.as_view(), name="modificar_articulo"),
    path("eliminar-articulo/<int:pk>", EliminarArticulo.as_view(), name="eliminar_articulo"),
    path("ver-articulo/<int:articulo_id>", ver_articulo, name="ver_articulo"),
    path("cambio-imagen/<int:articulo_id>", cambio_imagen, name="cambio_imagen"),
    path("about", about, name="about"),
]