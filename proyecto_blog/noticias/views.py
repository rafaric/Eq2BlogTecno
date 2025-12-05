from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia

# Create your views here.


def inicio(request):
    return render(request, "base.html")


def lista_noticias(request):
    contexto = Noticia.objects.all()
    suma = 1 + 1
    return render(request, "noticias/lista_noticias.html", {"noticias": contexto, "suma": suma})


def about(request):
    return HttpResponse("Esta es la página About de Noticias.")


def contacto(request):
    return render(request, "contacto.html")


# vistas con Clases


class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/lista_noticias.html"
    context_object_name = "noticias"


class DetalleNoticiaView(DetailView):
    model = Noticia
    template_name = "noticias/detalle_noticia.html"
    context_object_name = "noticia"
