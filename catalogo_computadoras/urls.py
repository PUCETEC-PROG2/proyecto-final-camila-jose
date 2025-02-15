from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('categoria/<str:categoria>/', views.productos_por_categoria, name='productos_categoria'),
    path('clientes/', views.clientes, name='clientes'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('compras/', views.compras, name='compras'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar-compra/', views.agregar_compra, name='agregar_compra'),
    path('compras/<int:id>/', views.detalle_compra, name='detalle_compra'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
]