from django import forms
from django.forms import widgets
from .models import Noticia, Comentario

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('autor', 'titulo', 'contenido', 'categorias')

        widgets ={
            'titulo': forms.TextInput(attrs={'class':'textIntputClass'}),
            'contenido': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class ComentarioForm(forms.Form):
        model = Comentario
        fields = ('cuerpo_comentario',)
        cuerpo_comentario = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control comment-textarea",
                "id":"comment",
                "placeholder": "Dinos que piensas, dejanos un comentario!"
            })
        )