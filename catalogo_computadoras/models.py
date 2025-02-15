from django.db import models

# Create your models here.

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
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.producto.nombre} por {self.cliente.nombre}"

