# Generated by Django 5.0.6 on 2024-05-31 04:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('expiration_date', models.DateField(verbose_name='Fecha de vencimiento')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Fabricante')),
                ('stock', models.IntegerField(verbose_name='Inventario')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Código del Medicamento')),
                ('unit', models.CharField(max_length=50, verbose_name='Unidad de Medida')),
                ('recommended_dosage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dosis Recomendada')),
                ('indications', models.TextField(blank=True, null=True, verbose_name='Indicaciones')),
                ('contraindications', models.TextField(blank=True, null=True, verbose_name='Contraindicaciones')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas Adicionales')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('categories', models.ManyToManyField(related_name='medications', to='medications.category', verbose_name='Categorías')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
