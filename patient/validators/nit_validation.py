import re
from django.core.exceptions import ValidationError

def has_valid_format(nit):
    """
    Verifica que el Número de Identificación Tributaria (NIT) tenga un formato válido.

    Parameters:
    nit (str): Número de Identificación Tributaria a validar.

    Returns:
    bool: True si el NIT tiene el formato válido #######K o #######k, False si no.

    Raises:
    ValueError: Si el parámetro nit es None.

    """
    # Expresión regular para validar el formato #######K o #######k
    expression = re.compile(r'^\d+[kK]?$')

    if nit is None:
        raise ValidationError("El NIT no puede ser nulo.")

    return expression.match(nit) is not None


def is_valid(nit):
    """
    Verifica que el Número de Identificación Tributaria (NIT) sea válido según el algoritmo del complemento 11.

    Parameters:
    nit (str): Número de Identificación Tributaria a validar.

    Returns:
    bool: True si el NIT es válido según el algoritmo del complemento 11, False si no.

    Raises:
    ValueError: Si el parámetro nit es None.
    ValueError: Si el NIT no tiene el formato válido #######K o #######k.

    """
    if nit is None:
        raise ValidationError("El NIT no puede ser nulo.")

    if not has_valid_format(nit):
        raise ValidationError("El NIT debe tener el formato #######K o #######k.")

    # Extraer número y dígito verificador
    number = nit[:-1]
    expected_checker = nit[-1].lower()

    factor = len(number) + 1
    total = 0

    # Calcular suma ponderada
    for i, char in enumerate(number):
        digit = int(char)
        total += digit * factor
        factor -= 1

    # Calcular módulo 11
    modulus = (11 - (total % 11)) % 11

    # Obtener dígito verificador esperado
    computed_checker = 'k' if modulus == 10 else str(modulus)

    return expected_checker == computed_checker