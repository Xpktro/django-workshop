from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    precio = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    codigo = models.CharField(max_length=5)
    activo = models.BooleanField(default=True)
    ingreso = models.DateField()

    def __unicode__(self):
        return self.nombre