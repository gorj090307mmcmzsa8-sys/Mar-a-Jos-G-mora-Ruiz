from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludo),         # Ruta /hola/
    path('inicio/', views.inicio),  # Ruta /hola/inicio/
]