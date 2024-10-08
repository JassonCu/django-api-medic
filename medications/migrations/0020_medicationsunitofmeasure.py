# Generated by Django 5.0.6 on 2024-08-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0019_alter_medicationspresentation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationsUnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Unidad de Medida')),
                ('short_name', models.CharField(max_length=10, unique=True, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medida',
                'ordering': ['name'],
            },
        ),
    ]
