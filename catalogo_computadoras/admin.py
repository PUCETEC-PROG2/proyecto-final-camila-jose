from django.contrib import admin
from .models import Producto, Cliente, Compra, DetalleCompra

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
    list_display = ('id', 'cliente', 'fecha', 'calcular_total')  # Campos válidos y método personalizado
    list_filter = ('fecha', 'cliente')  # Filtrar por fecha y cliente
    search_fields = ('cliente__nombre',)  # Permitir búsqueda por nombre del cliente

    def calcular_total(self, obj):
        return obj.calcular_total()
    calcular_total.short_description = 'Total'  # Nombre de la columna en el admin

@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'subtotal')
    list_filter = ('compra',)  # Filtrar por compra
    search_fields = ('compra__id', 'producto__nombre')  # Permitir búsqueda por ID de compra o nombre de producto