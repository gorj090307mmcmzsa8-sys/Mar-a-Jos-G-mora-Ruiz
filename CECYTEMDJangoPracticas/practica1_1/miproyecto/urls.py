from django.contrib import admin
from django.urls import path, include  # <- Importante incluir 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', include('hola.urls')),  # <- Incluye las URLs de la app 'hola'
]
