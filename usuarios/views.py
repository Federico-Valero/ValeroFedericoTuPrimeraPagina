from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import MiFormularioDeCreacion, MiFormularioDeEdicion
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

def login(request):
    
    if request.method == "POST":
        formulario= AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario= formulario.get_user()
            django_login(request,usuario)
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect("inicio")
    else:
        formulario= AuthenticationForm()
        
    return render(request, "login.html", {"formulario":formulario})
    
    
def registro(request):
    
    if request.method == "POST":
        formulario= MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario= MiFormularioDeCreacion()
        
    return render(request, "registro.html", {"formulario":formulario})

def editar_perfil(request):
    
    info_extra= request.user.infoextra
    
    if request.method == "POST":
        formulario= MiFormularioDeEdicion(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get("avatar"):
                info_extra.avatar= formulario.cleaned_data.get("avatar")
            if formulario.cleaned_data.get("fecha_nacimiento"):
                info_extra.fecha_nacimiento= formulario.cleaned_data.get("fecha_nacimiento")
            info_extra.save()
            formulario.save()
            return redirect("inicio")
    else:
        formulario= MiFormularioDeEdicion(instance= request.user, initial={"avatar":info_extra.avatar, "fecha_nacimiento":info_extra.fecha_nacimiento})
        
    return render(request, "editar_perfil.html", {"formulario":formulario})

def datos_usuario(request):
    
    return render(request, "datos_usuario.html")

class CambioPassworld(PasswordChangeView):
    template_name= "cambio_pass.html"
    success_url= reverse_lazy("inicio")