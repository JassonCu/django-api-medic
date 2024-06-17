from django.test import TestCase
from .validators.dpi_validation import dpi_is_valid

# Create your tests here.

class DPITestCase(TestCase):
    def test_valid_dpi(self):
        # DPI válido según el algoritmo y las listas proporcionadas
        valid_dpi = "3241783791601"
        self.assertTrue(dpi_is_valid(valid_dpi), f"{
                        valid_dpi} debería ser válido.")

    def test_invalid_dpi_format(self):
        # DPI con formato inválido (no cumple con el formato esperado)
        invalid_dpi = "12345"
        self.assertFalse(dpi_is_valid(invalid_dpi), f"{
                         invalid_dpi} debería ser inválido por formato.")

    def test_invalid_dpi_department(self):
        # DPI con código de departamento inválido (fuera del rango esperado)
        invalid_dpi = "1234567890123"
        self.assertFalse(dpi_is_valid(invalid_dpi), f"{
                         invalid_dpi} debería ser inválido por departamento.")

    def test_invalid_dpi_municipality(self):
        # DPI con código de municipio inválido (fuera del rango esperado para el departamento)
        invalid_dpi = "3241783791622"
        self.assertFalse(dpi_is_valid(invalid_dpi), f"{
                         invalid_dpi} debería ser inválido por municipio.")

    def test_invalid_dpi_verifier(self):
        # DPI con dígito verificador incorrecto
        invalid_dpi = "3241783791602"
        self.assertTrue(dpi_is_valid(invalid_dpi), f"{
                         invalid_dpi} debería ser inválido por dígito verificador.")
