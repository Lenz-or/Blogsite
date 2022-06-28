from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    path('crear-post/', crear_post, name='crear-post'),
    path('buscar-post/', buscar_post, name='buscar-post'),
    path('crear-usuario/',crear_usuario, name="crear-usuario"),
    path('crear-categoria/',crear_categoria, name="crear-categoria"),
]