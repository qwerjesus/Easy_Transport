from django.db import models

# Create your models here.

class Location( models.Model):
    name = models.CharField(max_length=250, verbose_name= 'Nombre de Ruta')
    addres = models.CharField(max_length=230, verbose_name= 'Direccion')
    latitude = models.FloatField(verbose_name='Latitud')
    length = models.FloatField(verbose_name='Longitud')

    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
        ordering = ['name']
    
    def __str__(self) :
        return self.name
