from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Ocupation(models.Model):
    name = models.CharField(
        _("Nombre"), max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

