from django.db import models

# Create your models here.

#Se trata de una página que consiste en carga de datos representativos a productos de farmacéutica

class medicamentos(models.Model):
    nombre = models.TextField()
    longitud = models.FloatField()
    ancho = models.FloatField()
    altura = models.FloatField()
    peso = models.FloatField()


class perfumeria(models.Model):
    nombre = models.TextField()
    longitud = models.FloatField()
    ancho = models.FloatField()
    altura = models.FloatField()
    peso = models.FloatField()

class suplementos(models.Model):
    nombre = models.TextField()
    longitud = models.FloatField()
    ancho = models.FloatField()
    altura = models.FloatField()
    peso = models.FloatField()
