from django.shortcuts import render, redirect
from .models import Imagen, Categoria, Video

# Create your views here.

def recursosindex(request):
    return render(request,'recursos-index.html',{})

def imagenesindex(request):
    lista_imagenes = Imagen.objects.all().order_by('publicado')
    context = {
    "imagenes": lista_imagenes,
    "MEDIA_ROOT": 'media/img/recursos/'
    }
    return render(request,'imagenes-index.html',context)

def videosvindex(request):
    lista_videos = Video.objects.all().order_by('publicado')
    context = {
    "videos": lista_videos,
    }
    return render(request,'videos-index.html',context)

def foto(request):
    return render(request,'foto.html',{})

def video(request):
    return render(request,'video.html',{})