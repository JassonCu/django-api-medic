# Generated by Django 5.0.6 on 2024-08-10 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0016_medicationcontraindication_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicationContraindication',
            new_name='MedicationContraindications',
        ),
    ]
