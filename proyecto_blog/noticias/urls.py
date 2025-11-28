from django.contrib import admin
from django.urls import path
from .views import about, contacto  # from . import views

urlpatterns = [
    path("", about, name="about"),
    path("contacto/", contacto, name="contacto")
]
