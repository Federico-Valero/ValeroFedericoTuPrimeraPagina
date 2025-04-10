from django.shortcuts import render, redirect
from inicio.models import Producto
from inicio.forms import CargarProducto, BuscarProducto, ModificarProducto, CambioImagen
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio.html")

@login_required
def cargar_articulo(request):
    formulario= CargarProducto()
    
    if request.method == "POST":
        formulario= CargarProducto(request.POST)
        if formulario.is_valid():
            precio= formulario.cleaned_data.get("precio")
            descripcion= formulario.cleaned_data.get("descripcion")
            stock= formulario.cleaned_data.get("stock")
            producto= Producto(precio= precio, descripcion= descripcion, stock= stock)
            producto.save()
            return redirect("lista_de_productos")
            
    return render(request, "cargar_articulo.html", {"formulario": formulario})


def lista_de_productos(request):
    articulos= Producto.objects.all()
    formulario= BuscarProducto(request.GET, request.FILES)
    
    if formulario.is_valid():
        articulo_a_buscar= formulario.cleaned_data.get("descripcion")
        articulos= Producto.objects.filter(descripcion__icontains= articulo_a_buscar)
        
    return render(request, "lista_de_productos.html", {"articulos":articulos, "formulario":formulario})

@login_required
def ver_articulo(request, articulo_id):
    articulo= Producto.objects.get(id=articulo_id)
    
    return render(request, 'ver_articulo.html', {"articulo": articulo})


class EliminarArticulo(LoginRequiredMixin, DeleteView):
    
    model = Producto
    template_name = "eliminar_articulo.html"
    success_url= reverse_lazy("lista_de_productos")


class ModificarArticulo(LoginRequiredMixin, UpdateView):
    
    model= Producto
    template_name= "modificar_articulo.html"
    form_class= ModificarProducto
    success_url= reverse_lazy("lista_de_productos")
    
def cambio_imagen(request, articulo_id):
    formulario= CambioImagen()
    producto= Producto.objects.get(id=articulo_id)
    if request.method == "POST":
        formulario= CambioImagen(request.POST, request.FILES)
        if formulario.is_valid():
            producto.imagen= formulario.cleaned_data.get("imagen")
            producto.save()
            return redirect("lista_de_productos")
    else:
        formulario= CambioImagen(initial={"imagen":producto.imagen})
    
    return render(request,"cambio_imagen.html",{"formulario":formulario})

def about(request):
    
    return render(request,"about.html")
