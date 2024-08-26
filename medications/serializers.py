from rest_framework import serializers
from .models import Medication, Category


class MedicationSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Medication
    """
    manufacturer_names = serializers.SerializerMethodField()
    class Meta:
        model = Medication
        fields = fields = [
            'id',
            'name',
            'description',
            'price',
            'currency',
            'expiration_date',
            'stock',
            'unit',
            #'unit_name',
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
        # Obtiene los nombres de los fabricantes
        manufacturers = obj.manufacturer.all()
        return [manufacturer.name for manufacturer in manufacturers]
    
class MedicationCategorySerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad MedicationCategory
    """
    class Meta:
        model = Category
        fields = '__all__'
