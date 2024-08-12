from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from bank.models import Currency

# Create your models here.


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


class MedicationsPresentation(models.Model):
    """
    Modelo de datos para las presentaciones de los medicamentos.
    """
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ["name"]
        verbose_name = _("Presentación")
        verbose_name_plural = _("Presentaciones")


class MedicationsManufacturer(models.Model):
    """
    Modelo de datos para los fabricantes de medicamentos.
    """
    name = models.CharField(_("Nombre"), max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Fabricante")
        verbose_name_plural = _("Fabricantes")


class MedicationsChemicalCompound(models.Model):
    """
    Modelo de datos para los compuestos químicos de los medicamentos.
    """
    name = models.CharField(max_length=100, unique=True,
                            verbose_name=_("Nombre"))
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Descripción"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Compuesto Químico")
        verbose_name_plural = _("Compuestos Químicos")


class MedicationsContraindications(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_("Nombre"), null=False, blank=False)

    def __str__(self):
        return self.name


class MedicationsUnitOfMeasure(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name=_("Unidad de Medida"))
    short_name = models.CharField(
        max_length=10, unique=True, verbose_name=_("Abreviatura"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Unidad de Medida")
        verbose_name_plural = _("Unidades de Medida")


class Medication(models.Model):
    """
    Modelo de datos para los medicamentos.
    """
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_("Nombre"), null=False, blank=False)
    description = models.TextField(
        blank=False, null=False, verbose_name=_("Descripción"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, verbose_name=_("Moneda"), null=True, blank=True)
    expiration_date = models.DateField(verbose_name=_(
        "Fecha de vencimiento"), null=False, blank=False)
    stock = models.CharField(verbose_name=_(
        "Inventario"), null=False, blank=False, max_length=255)
    unit = models.ForeignKey(
        'MedicationsUnitOfMeasure', on_delete=models.PROTECT, verbose_name=_("Unidad de Medida"))
    recommended_dosage = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Dosis Recomendada"), default='La que indique el médico')
    indications = models.TextField(
        blank=True, null=True, verbose_name=_("Indicaciones"), default='Las que indique el médico')
    notes = models.TextField(blank=True, null=True,
                             verbose_name=_("Notas Adicionales"))
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Fecha de actualización"))
    categories = models.ManyToManyField(
        'Category', related_name='medications', verbose_name=_("Categorías"), blank=False)
    presentation = models.ForeignKey(
        'MedicationsPresentation', on_delete=models.CASCADE, verbose_name=_("Presentación"))
    manufacturer = models.ManyToManyField(
        'MedicationsManufacturer', verbose_name=_("Fabricante"), blank=False)
    chemical_compound = models.ManyToManyField(
        'MedicationsChemicalCompound', blank=False, verbose_name=_("Compuesto Químico"))
    contraindications = models.ManyToManyField(
        'MedicationsContraindications', blank=False, verbose_name=_('Contraindicaciones'))

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
