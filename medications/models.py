from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.


class Medication(models.Model):
    """
    Modelo de datos para los medicamentos.
    """
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_("Nombre"), null=False, blank=False)
    description = models.TextField(
        blank=False, null=False, verbose_name=_("Descripción"))
    price = models.DecimalField(
        # cambiar a varchar
        max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    expiration_date = models.DateField(verbose_name=_(
        "Fecha de vencimiento"), null=False, blank=False)
    manufacturer = models.CharField(
        max_length=255, verbose_name=_("Fabricante"))
    stock = models.CharField(verbose_name=_(
        "Inventario"), null=False, blank=False, max_length=255)
    code = models.CharField(max_length=100, unique=False, verbose_name=_(
        "Compuesto químico"), null=False, blank=False)
    unit = models.CharField(max_length=100, verbose_name=_(
        "Unidad de Medida"), null=False, blank=False)
    recommended_dosage = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Dosis Recomendada"), default='La que indique el médico')
    indications = models.TextField(
        blank=True, null=True, verbose_name=_("Indicaciones"), default='Las que indique el médico')
    contraindications = models.TextField(
        blank=True, null=True, verbose_name=_("Contraindicaciones"))
    notes = models.TextField(blank=True, null=True,
                             verbose_name=_("Notas Adicionales"))
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Fecha de actualización"))
    categories = models.ManyToManyField(
        'Category', related_name='medications', verbose_name=_("Categorías"), blank=False)
    presentation = models.CharField(
        max_length=100, blank=False, null=False, verbose_name=_("Presentación"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]

    def save(self, *args, **kwargs):
        if not self.recommended_dosage:
            self.recommended_dosage = 'La que indique el médico'
        if not self.indications:
            self.indications = 'Las que indique el médico'
        super().save(*args, **kwargs)


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

class MedicationPresentation(models.Model):
    """
    Modelo de datos para las presentaciones de los medicamentos.
    """
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Presentación")
        verbose_name_plural = _("Presentaciones")