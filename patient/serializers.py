from rest_framework import serializers
from .models import Patient, Alergy, Ocupation

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AlergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergy
        fields = '__all__'

class OcupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupation
        fields = '__all__'
