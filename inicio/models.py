from django.db import models

class Producto(models.Model):
    precio= models.DecimalField(decimal_places=2, max_digits=10, default= 0.00)
    descripcion= models.CharField(max_length= 50)
    stock= models.BigIntegerField(default= 0)
    
    def __str__(self):
        return f"Producto: {self.descripcion}, Precio: ${self.precio}, Stock: {self.stock}"