# Generated by Django 5.0.6 on 2024-08-10 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0012_remove_medication_manufacturer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacturer',
            new_name='MedicationsManufacturer',
        ),
        migrations.RenameModel(
            old_name='MedicationPresentation',
            new_name='MedicationsPresentation',
        ),
    ]