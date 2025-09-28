from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo