from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    motivo = models.TextField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
