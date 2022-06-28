from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q

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


def crear_usuario(request):
    if request.method == "POST":

        info_formulario= request.POST
        
        usuario= Usuario(nombre = info_formulario["nombre"],apellido = info_formulario["apellido"],
        username = info_formulario["username"],email = info_formulario["email"])

        usuario.save()

        return redirect("inicio")
        
    #GET y otros
    else:
        return render(request,"ProyectoBlogApp/crear_usuario.html",{})

def crear_categoria(request):
    if request.method == "POST":

        info_formulario= request.POST
        
        categoria= Categoria(nombre = info_formulario["categoria"])

        categoria.save()

        return redirect("inicio")
        
    #GET y otros
    else:
        return render(request,"ProyectoBlogApp/crear_categoria.html",{})

def buscar_post(request):



   if request.method == "POST":



       post = request.POST["titulo"]
      
       titulos = Post.objects.filter( Q(titulo__icontains=post) ).values()



       return render(request,"ProyectoBlogApp/buscar_post.html",{"titulos":titulos})



   else: # get y otros



        titulos =  []  #Curso.objects.all()
      
        return render(request,"ProyectoBlogApp/buscar_post.html",{"titulos":titulos})


