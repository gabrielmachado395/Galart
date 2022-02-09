from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if any(numero.isdigit() for numero in nome):
            self.add_error(
                'nome_comentario',
                'Nome não pode ter números.'
            )

    
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')