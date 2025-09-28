from django.http import HttpResponse

def hola(request):
    return HttpResponse("<h1>Hola desde mi primera vista en Django</h1>")