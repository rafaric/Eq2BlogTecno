from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return HttpResponse("Esta es la página About de Noticias.")


def contacto(request):
    return render(request, "contacto.html")
