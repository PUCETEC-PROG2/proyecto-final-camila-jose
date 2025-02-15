from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('categoria/<str:categoria>/', views.productos_por_categoria, name='productos_categoria'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  # Asegúrate de que esta línea exista
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('compras/', views.compras, name='compras'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar-compra/', views.agregar_compra, name='agregar_compra'),
]