from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Producto
from inicio.forms import CargarProducto, BuscarProducto

def inicio(request):
    return render(request, "inicio.html")

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
    formulario= BuscarProducto(request.GET)
    if formulario.is_valid():
        articulo_a_buscar= formulario.cleaned_data.get("descripcion")
        articulos= Producto.objects.filter(descripcion__icontains= articulo_a_buscar)
    return render(request, "lista_de_productos.html", {"articulos":articulos, "formulario":formulario})
