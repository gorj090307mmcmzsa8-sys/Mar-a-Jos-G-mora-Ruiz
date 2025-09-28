from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'publicado')
    list_filter = ('publicado', 'fecha_creacion')
    search_fields = ('titulo', 'autor')

admin.site.register(Post, PostAdmin)
