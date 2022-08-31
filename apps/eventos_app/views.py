from django.shortcuts import render
from .models import Evento,Categoria
from django.http.response import Http404
from apps.noticias_app.models import Noticia, Comentario, Categoria
from apps.contacto_app.models import Contacto

# Create your views here.

def index(request):
    lista_noticias = Noticia.objects.all().order_by('-creado')[:3]
    lista_eventos = Evento.objects.all().order_by('-fecha')[:3]
    context = {
        "noticias": lista_noticias,
        "eventos": lista_eventos,
    }
    return render(request, 'index.html', context)


def contacto(request):
    if request.method == "POST":
        contacto = Contacto()
        nombre = request.POST.get('name')
        email = request.POST.get('email')
        motivo = request.POST.get('subject')
        mensaje = request.POST.get('message')
        contacto.nombre = nombre
        contacto.email = email
        contacto.motivo = motivo
        contacto.mensaje = mensaje
        contacto.save()
        return render(request, 'contacto/contactos.html')
    return render(request, 'contacto/contacto.html')

def eventos(request):
    lista_eventos = Evento.objects.all().order_by('fecha')
    context = {
        "eventos": lista_eventos,
        "MEDIA_ROOT": '',
    }
    return render(request, 'eventos.html', context)

def eventosdetalle(request, id):
    try:
        dataevento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        raise Http404('El evento solicitada no existe.')

    context = {
        "evento": dataevento,
        "MEDIA_ROOT": '',
    }

    return render (request, 'detalleEvento.html',context)

def nosotros(request):
        return render(request, 'nosotros.html')

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