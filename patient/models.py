from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .validators.dpi_validation import dpi_is_valid

# Create your models here.


class Ocupation(models.Model):
    """
    Modelo que se encarga de almacenar todas las ocupaciones.
    """
    name = models.CharField(
        _('Nombre'), max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = _('Ocupación')
        verbose_name_plural = _('Ocupaciones')


class Alergy(models.Model):
    """
    Modelo para alergias.
    """
    name = models.CharField(
        _('Nombre'), max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Alergía')
        verbose_name_plural = _('Alergias')

class Patient(models.Model):
    """
    Modelo para guardar la información de los pacientes.
    """
    name = models.CharField(
        _('Nombre del paciente'), max_length=100, null=False, blank=False)
    last_name = models.CharField(
        _('Apellido del paciente'), max_length=100, null=False, blank=False)
    age = models.SmallIntegerField(
        _('Edad del paciente'), null=False, blank=False)
    birth_date = models.DateField(
        _('Fecha de nacimiento del paciente'), null=False, blank=False)
    dpi = models.CharField(
        _('DPI del paciente'), max_length=13, null=True, blank=True, validators=[dpi_is_valid])
    gender = models.CharField(
        _('Género del paciente'), max_length=10, null=False, blank=False, choices=[
            ('M', 'Masculino'), ('F', 'Femenino'),])
    address = models.CharField(
        _('Dirección del paciente'), max_length=100, null=False, blank=False)
    phone = models.CharField(
        _('Teléfono del paciente'), max_length=20, null=True, blank=True)
    email = models.EmailField(
        _('Correo electrónico del paciente'), null=True, blank=True)
    blood_group = models.CharField(
        _('Grupo sanguíneo del paciente'), max_length=3, null=True, blank=True, choices=[
            ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    history = models.TextField(
        _('Historia del paciente'), max_length=500, null=True, blank=True)
    civil_status = models.CharField(
        _('Estado civíl'), max_length=25, null=False, blank=False, choices=[
            ('Soltero', 'Soltera'), ('Casado', 'Casada'), ('Divorciado', 'Divorciada'), ('Viudo', 'Viuda')])
    ocupation = models.ManyToManyField(
        Ocupation, verbose_name=_("Ocupación"), related_name="patients", blank=False)
    created_at = models.DateTimeField(
        _('Fecha de registro'), default=timezone.now)
    updated_at = models.DateTimeField(
        _('Fecha de actualización'), default=timezone.now)
    bring_medical_prescription = models.BooleanField(
        _('Trae Receta Médica'), default=False,)
    is_alergic = models.BooleanField(
        _('Es Alergico'), default=False)
    is_alergic_to = models.TextField(
        _('Es Alergico a'), blank=True, null=True,)
    weight = models.DecimalField(
        _('Peso'), max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(
        _('Altura'), max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = _("Paciente")
        verbose_name_plural = _("Pacientes")
