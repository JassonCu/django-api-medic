from rest_framework import serializers
from .models import Medication, Category


class MedicationSerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad Medication
    """
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationCategorySerializer(serializers.ModelSerializer):
    """
    Serializer para la entidad MedicationCategory
    """
    class Meta:
        model = Category
        fields = '__all__'
