from django import forms
from inicio.models import Producto

class CargarProducto(forms.Form):
    precio= forms.DecimalField(decimal_places=2, max_digits=10)
    descripcion= forms.CharField(max_length=50)
    stock= forms.IntegerField()
    
    
class BuscarProducto(forms.Form):
    descripcion= forms.CharField(max_length=50, required= False)
    
class ModificarProducto(forms.ModelForm):
    fecha_creacion= forms.DateField(required=False, widget=forms.DateInput(attrs={"type":"date"}))
    
    class Meta:
        model= Producto
        fields= ["precio","descripcion","stock","fecha_creacion"]

class CambioImagen(forms.Form):
    imagen= forms.ImageField(required=False)