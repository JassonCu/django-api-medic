from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class Medication(models.Model):
    """
    Modelo de datos para los medicamentos.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    expiration_date = models.DateField(verbose_name=_("Fecha de vencimiento"))
    manufacturer = models.CharField(max_length=255, verbose_name=_("Fabricante"))
    stock = models.IntegerField(verbose_name=_("Inventario"))
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Código del Medicamento"))
    unit = models.CharField(max_length=50, verbose_name=_("Unidad de Medida"))
    recommended_dosage = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Dosis Recomendada"))
    indications = models.TextField(blank=True, null=True, verbose_name=_("Indicaciones"))
    contraindications = models.TextField(blank=True, null=True, verbose_name=_("Contraindicaciones"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notas Adicionales"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Fecha de actualización"))
    categories = models.ManyToManyField('Category', related_name='medications', verbose_name=_("Categorías"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Category(models.Model):
    """
    Modelo de datos para las categorías de los medicamentos.
    """
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")
