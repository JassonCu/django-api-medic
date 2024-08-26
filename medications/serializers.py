from rest_framework import serializers
from .models import Medication, Category


class MedicationSerializer(serializers.ModelSerializer):
    manufacturer_names = serializers.SerializerMethodField()
    currency_symbol = serializers.SerializerMethodField()  # Agregado

    class Meta:
        model = Medication
        fields = [
            'id',
            'name',
            'description',
            'price',
            'currency',
            'currency_symbol',
            'expiration_date',
            'stock',
            'unit',
            'recommended_dosage',
            'indications',
            'notes',
            'created_at',
            'updated_at',
            'categories',
            'presentation',
            'manufacturer',
            'manufacturer_names',
            'chemical_compound',
            'contraindications'
        ]

    def get_manufacturer_names(self, obj):
        manufacturers = obj.manufacturer.all()
        return [manufacturer.name for manufacturer in manufacturers]

    def get_currency_symbol(self, obj):
        return obj.currency.symbol if obj.currency else ''

    
class MedicationCategorySerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad MedicationCategory
    """
    class Meta:
        model = Category
        fields = '__all__'
