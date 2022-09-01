from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__ (self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/eventos',help_text="Seleccione una imagen para mostrar")
    fecha = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', related_name='evento')
    modalidad = models.TextField()
    lugar = models.TextField()
    precio = models.CharField(max_length=50)

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()
