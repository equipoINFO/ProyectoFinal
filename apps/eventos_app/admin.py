from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import Categoria, Evento

class CategoriasInline(admin.StackedInline):
    model: Evento.categorias.through
    extra= 5

class EventosAdmin(admin.ModelAdmin):
    model: Evento
    inlines: (CategoriasInline)
    raw_id_fields = ("categorias",)
    list_display = ('titulo', 'img')
    search_fields = ('titulo', 'creado')

    list_per_page = 15

    readonly_fields = ['evento_img']

    def categoria(self, obj):
        return "\n".join([c.nombre for c in obj.categorias.all()])

    def evento_img(self,obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url)
        )

admin.site.register(Categoria,admin.ModelAdmin)
admin.site.register(Evento,EventosAdmin)