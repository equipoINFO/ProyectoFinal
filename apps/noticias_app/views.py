#from multiprocessing import context
from contextvars import Context
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Noticia,Categoria,Comentarios
from django.http.response import Http404
# Create your views here.

def index(request):
    lista_noticias = Noticia.objects.all().order_by('-creado')[:3]
    lista = {
         "noticia": lista_noticias,
    }
    return render(request,'index1.html',lista)#context={},)

	#lista_noticias = Noticia.objects.all().order_by('-creado')[: 3]
	#if not bool(lista_noticias):
    #		lista = {
    #    		"noticia": lista_noticias,
	#			}
	#else:
    #		lista = {
    #    		"noticia": "lista_noticias",
	#			}
	#return render(request, 'index1.html', lista)


def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request,id):
    try:
        datanoticia = Noticia.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios
    }

    return render(request,'detalle-noticia.html',context)

