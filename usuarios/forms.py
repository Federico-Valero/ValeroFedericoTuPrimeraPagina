from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class MiFormularioDeCreacion(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields= ["username","email","password1","password2"]
        help_texts= {field: "" for field in fields}
        
class MiFormularioDeEdicion(UserChangeForm):
    password= None
    email= forms.EmailField()
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    avatar= forms.ImageField(required=False, label="Imagen de avatar")
    fecha_nacimiento= forms.DateField(required=False, widget=forms.DateInput(attrs={"type":"date"}))
    
    class Meta:
        model= User
        fields= ["email","first_name","last_name","avatar","fecha_nacimiento"]