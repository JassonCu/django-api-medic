# Generated by Django 5.0.6 on 2024-08-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0011_manufacturer_alter_medication_manufacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='presentation',
        ),
        migrations.AddField(
            model_name='medication',
            name='manufacturer',
            field=models.ManyToManyField(to='medications.manufacturer', verbose_name='Fabricante'),
        ),
        migrations.AddField(
            model_name='medication',
            name='presentation',
            field=models.ManyToManyField(to='medications.medicationpresentation', verbose_name='Presentación'),
        ),
    ]