from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    path('crear-post/', crear_post, name='crear-post'),
    path('buscar-post/', buscar_post, name='buscar-post'),
]