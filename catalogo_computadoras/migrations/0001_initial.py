# Generated by Django 4.2 on 2025-02-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_computadoras.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('categoria', models.CharField(choices=[('laptops', 'Laptops/Notebooks'), ('hardware', 'Hardware'), ('escritorio', 'Computadoras de Escritorio')], default='laptops', max_length=20)),
                ('destacado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_computadoras.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_computadoras.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(through='catalogo_computadoras.DetalleCompra', to='catalogo_computadoras.producto'),
        ),
    ]
