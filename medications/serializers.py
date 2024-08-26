from rest_framework import serializers
from .models import Medication, Category, MedicationsPresentation


class MedicationSerializer(serializers.ModelSerializer):
    manufacturer_names = serializers.SerializerMethodField()
    currency_symbol = serializers.SerializerMethodField()  # Agregado
    unit_short_name = serializers.SerializerMethodField()
    presentation_name = serializers.SerializerMethodField()

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
            'unit_short_name',
            'recommended_dosage',
            'indications',
            'notes',
            'created_at',
            'updated_at',
            'categories',
            'presentation',
            'presentation_name',
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

    def get_unit_short_name(self, obj):
        return obj.unit.short_name if obj.unit else ''
    
    def get_presentation_name(self, obj):
        return obj.presentation.name if obj.presentation else ''

class MedicationCategorySerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad MedicationCategory
    """
    class Meta:
        model = Category
        fields = '__all__'
