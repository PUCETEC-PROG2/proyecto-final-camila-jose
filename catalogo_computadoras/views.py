from django.shortcuts import render, redirect
from .models import Producto, Cliente, Compra
from .forms import ClienteForm
from .forms import CompraForm


# Create your views here.

def inicio(request):
    # Obtener los productos filtrados por destacados
    productos_destacados = Producto.objects.filter(destacado=True)
    return render(request, 'inicio.html', {'productos_destacados': productos_destacados})

def productos_por_categoria(request, categoria):
    # Obtener los productos filtrados por categoría
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'productos_categoria.html', {'productos': productos, 'categoria': categoria})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras.html', {'compras': compras})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compras')
    else:
        form = CompraForm()
    return render(request, 'agregar_compra.html', {'form': form})

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:   
        form = ClienteForm(instance=cliente)
    return render(request, 'agregar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')
