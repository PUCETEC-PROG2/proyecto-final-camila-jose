from django.db import models
from django.shortcuts import render

class Producto(models.Model):
    CATEGORIAS = [
        ('laptops', 'Laptops/Notebooks'),
        ('hardware', 'Hardware'),
        ('escritorio', 'Computadoras de Escritorio'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='laptops')
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)  
    productos = models.ManyToManyField(Producto, through='DetalleCompra')

    def __str__(self):
        return f"Compra {self.id} - {self.cliente.nombre}"
    
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"
