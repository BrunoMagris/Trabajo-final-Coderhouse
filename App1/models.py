from mailbox import NoSuchMailboxError
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Restaurante(models.Model):
    Nombre = models.CharField(max_length=60)
    Localizacion = models.CharField(max_length=60)
    Categoria = models.CharField(max_length=60)
    Especialidad = models.CharField(max_length=60)
    Reseña = models.CharField(max_length=200)

class Recomendaciones(models.Model):
    Nombre = models.CharField(max_length=60)
    Localizacion = models.CharField(max_length=60)
    Categoria = models.CharField(max_length=60)
    Especialidad = models.CharField(max_length=60)
    Reseña = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to = "recomendaciones", null=True, blank=True)