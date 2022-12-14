from django.shortcuts import render, redirect
from .models import Contacto

# Create your views here.

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
