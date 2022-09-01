from django.shortcuts import render, redirect
from .models import Evento,Categoria
from django.http.response import Http404

# Create your views here.

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
