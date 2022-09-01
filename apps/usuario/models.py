from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from pickletools import UP_TO_NEWLINE


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.usuario.save()