from django.contrib import admin
from .models import Producto, Cliente, Compra

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'destacado')  # Campos que se mostrarán en la lista de productos
    list_editable = ('destacado',)  # Permitir editar el campo "destacado" directamente desde la lista
    search_fields = ('nombre',)  # Permitir búsqueda por nombre
    list_filter = ('destacado',)  # Filtrar productos por el campo "destacado"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'fecha', 'cantidad', 'total')