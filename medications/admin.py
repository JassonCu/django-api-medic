from django.contrib import admin
from .models import Medication, Category

# Register your models here.

admin.site.register(Medication)
admin.site.register(Category)
