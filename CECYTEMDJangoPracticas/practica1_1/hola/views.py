from django.shortcuts import render

def saludo(request):
    return render(request, 'saludo.html')

def inicio(request):
    return render(request, 'inicio.html')