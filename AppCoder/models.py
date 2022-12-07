from django.db import models

# Create your models here.
class Familiar(models.Model):
    #---------------------------------------------------------------------------
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaport = models.IntegerField()
    #---------------------------------------------------------------------------
    def _str_(self):
        return f"{self.nombre}, {self.numero_pasaport}, {self.id}"