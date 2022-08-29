from distutils.command.upload import upload
from pickletools import UP_TO_NEWLINE
from pyexpat import model
from statistics import mode
from time import timezone
from datetime import datetime
from tokenize import blank_re
from unicodedata import category
from xml.dom import NoModificationAllowedErr
from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)


class Noticia(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/noticias',
                            help_text='seleccione una imagen para mostrar')
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    pubicado = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField('Categoria', related_name='noticias')

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()

    def comentariosAprobados(self):
        return self.comentarios.filter(aprobados=True)


class Comentario(models.Model):
    noticia = models.ForeignKey(
        'Noticia', related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)

    def aprobarcomentario(self):
        self.aprobado = True
        self.save()
