from django.contrib import admin
from .models import Categoria,Imagen,Video

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Imagen)
admin.site.register(Video)