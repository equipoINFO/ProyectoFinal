from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__ (self):
        return self.nombre

class Imagen(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo=models.CharField(null=True,max_length=255)
    img=models.ImageField(null=False,blank=False,upload_to='img/noticias',help_text="seleccione una imagen")
    publicado=models.DateTimeField(blank=True,null=True)
    categorias=models.ManyToManyField('Categoria',related_name='imágenes',blank=True)

class Video(models.Model):
    autor=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo=models.CharField(null=False,max_length=50)
    vid=models.FileField(null=False,upload_to='videos/recursos',validators=[FileExtensionValidator(['MOV','avi','mp4','webm','mkv'],'No supported format')])
    publicado=models.DateTimeField(blank=True,null=True)
    categorias=models.ManyToManyField('Categoria',related_name='videos',blank=True)