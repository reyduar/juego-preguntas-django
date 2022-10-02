from django import forms


class FormPregunta(forms.Form):
    niveles_options = [(1, 'Fácil'), (2, 'Medio'), (3, 'Master')]
    nivelId = forms.TypedChoiceField(label="Nivel", choices=niveles_options)
    categoriaId = forms.IntegerField(label="Categoria")
    pregunta = forms.CharField(label="Pregunta")
    imagen = forms.CharField(label="Imagen Url", widget=forms.Textarea)
