from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Post,Usuario,Categoria



# Create your views here.

def inicio(request):

        return render(request,"ProyectoBlogApp/index.html",{})

def crear_post(request):
    if request.method == "POST":

        info_formulario= request.POST
        
        post= Post(titulo = info_formulario["titulo"],contenido = info_formulario["contenido"])

        post.save()

        return redirect("inicio")
        
    #GET y otros
    else:
        return render(request,"ProyectoBlogApp/crear_post.html",{})