from django.contrib import admin
from django.urls import path
from .views import inicio, about, contacto, lista_noticias  # from . import views
from .views import NoticiaListView, DetalleNoticiaView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("contacto/", contacto, name="contacto"),
    # path("noticias/", lista_noticias, name="lista_noticias")
    path("noticias/", NoticiaListView.as_view(), name="lista_noticias"),
    path("noticias/<int:pk>", DetalleNoticiaView.as_view(), name="noticia_detalle")

]
