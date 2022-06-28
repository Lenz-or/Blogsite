from django.contrib import admin

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'contenido',)
    search_fields = ('titulo',)

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido','username','email',)
    search_fields = ('nombre', 'username',)

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nombre',)


admin.site.register(Post, PostAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)

