from django.shortcuts import render, redirect
from django.http.response import Http404
from .models import Noticia,Categoria,Comentario
from apps.eventos_app.models import Evento,Categoria
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)

# Create your views here.

def index(request):
   lista_noticias = Noticia.objects.all().order_by('-creado')[:3]
   lista_eventos = Evento.objects.all().order_by('-fecha')[:3]
   context = {
      "noticias": lista_noticias,
      "eventos": lista_eventos,
   }
   return render(request, 'index.html', context)


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
   
   form=ComentarioForm()

   if (request.method == "POST") and (request.user.id !=None):
      form = ComentarioForm(request.POST)
      if form.is_valid():
         comment = Comentario(
            autor_id = request.user.id,
            cuerpo_comentario = form.cleaned_data["cuerpo_comentario"],
            noticia = datanoticia
         )
         comment.save()
         return redirect("noticiasdetalle", id=datanoticia.id)
      
   context = {
      "noticia": datanoticia,
      "comentarios":lista_comentarios,
      "formulario": form,
   }

   return render (request, 'detalleNoticia.html',context)

class CrearNoticiaView(CreateView, LoginRequiredMixin):
   login_url= '/login'

   form_class = NoticiaForm

   model = Noticia


   def blog_categoria(request, categoria):
      posts = Noticia.objects.filter(
            categories__name__contains=categoria
      ).order_by(
            'creado'
      )
      context = {
            "categoria": categoria,
            "posts": posts
      }
      return render(request, "blog_categoria.html", context)


@login_required
def post_publish(request, id):
   try:
      noticias =Noticia.objects.get(id =id)
   except Noticia.DoesNotExist:
      raise Http404('No existe la noticia')
   
   Noticia.publish()
   return redirect('detalle-noticia', id=id)


@login_required
def comment_approve(request, id):
   try:
      comentarios =Comentario.objects.get(id =id)
   except Comentario.DoesNotExist:
      raise Http404('Comentario no existe')
   comentarios.approve()
   return redirect('noticiasdetalle', id=comentarios.noticia.id)


@login_required
def comment_remove(request, id):
   try:
      comentario =Comentario.objects.get(id =id)
   except Comentario.DoesNotExist:
      raise Http404('Comentario no existe')
   noticia_id = comentario.noticia.id
   comentario.delete()
   return redirect('noticiasdetalle', id=noticia_id)

def nosotros(request):
      return render(request, 'nosotros.html')
