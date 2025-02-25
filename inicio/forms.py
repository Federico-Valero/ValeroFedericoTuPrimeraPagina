from django import forms

class CargarProducto(forms.Form):
    precio= forms.DecimalField(decimal_places=2, max_digits=10)
    descripcion= forms.CharField(max_length=50)
    stock= forms.IntegerField()
    
class BuscarProducto(forms.Form):
    descripcion= forms.CharField(max_length=50, required= False)