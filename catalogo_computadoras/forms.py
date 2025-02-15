from django import forms
from .models import Cliente, Compra, Producto, DetalleCompra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu número de teléfono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu dirección'})
        }

class CompraForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Compra
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        compra = super().save(commit=commit)
        productos = self.cleaned_data['productos']
        for producto in productos:
            DetalleCompra.objects.create(compra=compra, producto=producto, cantidad=1)  
        return compra