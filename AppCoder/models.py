from django.db import models

# Create your models here.
class Familiar(models.Model):
    #---------------------------------------------------------------------------
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    #creado_el = models.DateField(auto_created = True)
    #---------------------------------------------------------------------------
    def _str_(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"
    #---------------------------------------------------------------------------
#---------------------------------------------------------------------------