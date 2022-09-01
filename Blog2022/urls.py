"""Blog2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from apps.contacto_app import views as viewsContacto
from apps.recursos_app import views as viewsRecursos
from apps.eventos_app import views as viewsEventos
from apps.noticias_app import views as viewsNoticias


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', viewsNoticias.index, name='index'),
    path('contacto', viewsContacto.contacto, name='contacto'),
    path('nosotros', viewsNoticias.nosotros, name='nosotros'),
    path('eventos', viewsEventos.eventos, name='eventos'),
    path('eventos/<int:id>/', viewsEventos.eventosdetalle, name='eventosdetalle'),
    path('noticias', viewsNoticias.noticias, name='noticias'),
    path('noticias/<int:id>/', viewsNoticias.noticiasdetalle, name='noticiasdetalle'),
    path("noticias/new", viewsNoticias.CrearNoticiaView.as_view(), name='CrearNoticiaView'),
    path('comentario/<int:id>/approve', viewsNoticias.comment_approve, name='comment_approve'),
    path('comentario/<int:id>/remove', viewsNoticias.comment_remove, name='comment_remove'),
    path('recursos', viewsRecursos.recursosindex, name='recursosindex'),
    path('imagenes', viewsRecursos.imagenesindex, name='Imágenes'),
    path('foto',viewsRecursos.foto,name='foto'),
    path('videos',viewsRecursos.videosvindex,name='Videos'),
    path('video',viewsRecursos.video,name='video'),
    path('registration/', include('apps.usuario.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
