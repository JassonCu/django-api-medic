from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Currency(models.Model):
    code = models.CharField(_('Código'), max_length=3, unique=True)
    name = models.CharField(_('Nombre'), max_length=100, unique=True)
    symbol = models.CharField(_('Símbolo'), max_length=1, unique=True)

    def __str__(self):
        return self.name