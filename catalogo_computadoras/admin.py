from django.contrib import admin
from .models import Producto, Cliente, Compra, DetalleCompra

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'destacado')  
    list_editable = ('destacado',)  
    search_fields = ('nombre',)  
    list_filter = ('destacado',)  

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion')



@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'subtotal')
    list_filter = ('compra',)  
    search_fields = ('compra__id', 'producto__nombre')  