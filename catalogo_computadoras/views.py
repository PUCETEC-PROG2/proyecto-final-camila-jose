from django.shortcuts import render, redirect
from .models import Producto, Cliente, Compra, DetalleCompra
from .forms import ClienteForm
from decimal import Decimal

def inicio(request):
    productos_destacados = Producto.objects.filter(destacado=True)
    return render(request, 'inicio.html', {'productos_destacados': productos_destacados})

def productos_por_categoria(request, categoria):
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'productos_categoria.html', {'productos': productos, 'categoria': categoria})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def compras(request):
    compras = Compra.objects.all().order_by('-fecha')  
    return render(request, 'compras.html', {'compras': compras})

def acerca_de(request):
    return render(request, 'acerca_de.html')

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
        cliente_id = request.POST.get('cliente')
        fecha = request.POST.get('fecha')
        producto_ids = request.POST.getlist('productos')

        productos_seleccionados = Producto.objects.filter(id__in=producto_ids)
        total = Decimal('0.00') 
        for producto in productos_seleccionados:
            total += producto.precio  

        cliente = Cliente.objects.get(id=cliente_id)
        compra = Compra.objects.create(cliente=cliente, fecha=fecha, total=total)
        compra.productos.set(productos_seleccionados)  

        return redirect('compras')  

    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'agregar_compra.html', {
        'clientes': clientes,
        'productos': productos,
    })

def detalle_compra(request, id):
    compra = Compra.objects.get(id=id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'detalle_compra.html', {
        'compra': compra,
        'detalles': detalles,
    })

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

def buscar_productos(request):
    query = request.GET.get('q')  
    resultados = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'buscar.html', {'query': query, 'resultados': resultados})