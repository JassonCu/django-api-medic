from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Medication

# Create your tests here.


class MedicationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.medication1 = Medication.objects.create(
            name="Amoxicilina",
            description="Antibiótico de amplio espectro usado para tratar infecciones bacterianas.",
            price="10.00",
            expiration_date="2025-03-26",
            manufacturer="Farmacéutica XYZ",
            stock=5,
            code="AMX789",
            unit="mg",
            recommended_dosage="Según las indicaciones del médico.",
            indications="Tratamiento de infecciones bacterianas como sinusitis, otitis media, infecciones de la piel, etc.",
            contraindications="No usar en caso de alergia a la penicilina.",
            notes="Tomar con alimentos para reducir el malestar estomacal."
        )
        self.medication2 = Medication.objects.create(
            name="Omeprazol",
            description="Inhibidor de la bomba de protones utilizado para tratar úlceras y enfermedades relacionadas con el ácido del estómago.",
            price="10.00",
            expiration_date="2025-03-26",
            manufacturer="Laboratorios DEF",
            stock=46,
            code="OMP456",
            unit="mg",
            recommended_dosage="20 mg una vez al día, preferiblemente en la mañana antes del desayuno.",
            indications="Tratamiento de úlceras gástricas y duodenales, reflujo gastroesofágico, etc.",
            contraindications="No usar en caso de alergia al omeprazol o a otros inhibidores de la bomba de protones.",
            notes="Evitar el consumo excesivo de cafeína y alimentos picantes."
        )
        self.medication3 = Medication.objects.create(
            name="Penicilina",
            description="No se para que sirve realemente pero si sirve.",
            price="10.00",
            expiration_date="2025-03-26",
            manufacturer="Laboratorios DEFE-CTUOSO",
            stock=46,
            code="OMP456333",
            unit="mg",
            recommended_dosage="Inyeccciones de esas de cinco centimetros creo.",
            indications="No es para todo el mundo.",
            contraindications="Creo que hay gente alergica a este medicamento.",
            notes="Evitar el consumo excesivo de cafeína y alimentos picantes."
        )
    def test_list_medications(self):
        # Asegúrate de usar el nombre correcto de la URL
        url = reverse('medication-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica que se devuelvan todas las medicaciones
        self.assertEqual(len(response.data), 3)
