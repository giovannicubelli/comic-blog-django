from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget # Para usar CKEditor en el form

class PostForm(forms.ModelForm):
    # Si quieres personalizar el widget de contenido para CKEditor explícitamente
    # contenido = forms.CharField(widget=CKEditorWidget()) # Ya lo hace por defecto si el modelo usa RichTextField

    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'editorial'] # Campos que se mostrarán en el form
        # Opcionalmente, personaliza widgets o labels:
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del cómic/post'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lema o subtítulo (opcional)'}),
            # CKEditor se aplica automáticamente al RichTextField
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Marvel, DC, Image'}),
        }
        labels = {
            'titulo': 'Título Principal',
            'subtitulo': 'Subtítulo',
            'contenido': 'Descripción / Reseña del Cómic',
            'imagen': 'Portada del Cómic',
            'editorial': 'Editorial del Cómic'
        }