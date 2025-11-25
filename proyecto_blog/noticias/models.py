from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# Tablas de nuestra base de datos


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="noticias")
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to="noticias", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
