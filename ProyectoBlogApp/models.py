from django.db import models

# Create your models here.

class Post(models.Model):

    # id por defecto
    titulo = models.CharField(max_length=30) # Texto
    contenido = models.CharField(max_length=150)

class Usuario(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    username = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

class Categoria(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Textol