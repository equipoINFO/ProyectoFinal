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
from apps.contacto_app import views
from apps.recursos_app import views
from apps.eventos_app import views
from apps.noticias_app import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('eventos', views.eventos, name='eventos'),
    path('eventos/<int:id>/', views.eventosdetalle, name='eventosdetalle'),
    path('noticias', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.noticiasdetalle, name='noticiasdetalle'),
    path("noticias/new", views.CrearNoticiaView.as_view(), name='CrearNoticiaView'),
    path('comentario/<int:id>/approve', views.comment_approve, name='comment_approve'),
    path('comentario/<int:id>/remove', views.comment_remove, name='comment_remove'),
    path('noticia/<int:id>/comentar', views.agregar_comentario, name='agregar_comentario'),
    path('recursos', views.recursosindex, name='recursosindex'),
    path('imagenes', views.imagenesindex, name='Imágenes'),
    path('foto',views.foto,name='foto'),
    path('videos',views.videosvindex,name='Videos'),
    path('video',views.video,name='video'),
    path('registration/', include('apps.usuario.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
