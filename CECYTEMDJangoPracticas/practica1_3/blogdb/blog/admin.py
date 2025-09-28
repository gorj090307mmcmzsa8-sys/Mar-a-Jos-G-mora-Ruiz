from django.contrib import admin
from .models import Post  # Importamos el modelo Post

admin.site.register(Post)  # Lo registramos en el panel de admin

