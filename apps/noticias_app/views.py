from django.shortcuts import render
from django.http.response import Http404
from .models import Noticia,Categoria,Comentario

# Create your views here.

def index(request):
	return render(request, 'base.html')


def contacto(request):
      return render(request, 'contacto/contacto.html')

def noticias(request):
   lista_noticias = Noticia.objects.all().order_by('creado')
   context = {
      "noticias": lista_noticias,
   }
   return render(request, 'noticias.html', context)

def noticiasdetalle(request, id):
   try:
      datanoticia = Noticia.objects.get(id=id)
      lista_comentarios = Comentario.objects.filter(aprobado=True)
   except Noticia.DoesNotExist:
      raise Http404('La noticia solicitada no existe.')
   
   context = {
      "noticia": datanoticia,
      "comentarios": lista_comentarios
   }

   return render (request, 'detalleNoticia.html',context)
