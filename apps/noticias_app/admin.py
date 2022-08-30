from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import Categoria, Comentario, Noticia

class CategoriasInline(admin.StackedInline):
    model: Noticia.categorias.through
    extra= 5

class NoticiasAdmin(admin.ModelAdmin):
    model: Noticia
    inlines: (CategoriasInline)
    raw_id_fields = ("categorias",)
    list_display = ('titulo', 'autor', 'img')
    search_fields = ('titulo', 'autor', 'creado')

    list_per_page = 15

    readonly_fields = ['noticia_img']

    def categoria(self, obj):
        return "\n".join([c.nombre for c in obj.categorias.all()])

    def noticia_img(self,obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url)
        )

admin.site.register(Categoria,admin.ModelAdmin)
admin.site.register(Noticia,NoticiasAdmin)

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('autor','cuerpo_comentario','noticia','aprobado')
    list_filter = ('aprobado', 'creado')
    search_fields = ('autor','cuerpo_comentario')
    actions = ['aprobar_comentarios']

    def aprobar_comentarios(self,request,queryset):
        queryset.update(aprobado=True)

admin.site.register(Comentario,ComentariosAdmin)