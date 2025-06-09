from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # Importar CKEditor

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo/Lema", blank=True, null=True) # CharField adicional
    # contenido = models.TextField(verbose_name="Contenido") # Reemplazado por CKEditor
    contenido = RichTextField(verbose_name="Contenido del Post (Descripción del cómic, reseña, etc.)")
    imagen = models.ImageField(upload_to='posts_images/', verbose_name="Imagen de Portada", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Autor")
    # Campo CharField adicional (ej: Editorial o Género)
    editorial = models.CharField(max_length=100, verbose_name="Editorial", blank=True)

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
# Create your models here.
