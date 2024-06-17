import re

def dpi_is_valid(dpi) -> bool:
    """
    Valida un número de DPI (Documento Personal de Identificación) guatemalteco.

    Args:
    dpi (str): Número de DPI en formato string. Puede incluir espacios.

    Returns:
    bool: True si el DPI es válido, False en caso contrario.

    La función realiza las siguientes validaciones:
    1. Verifica que el DPI no esté vacío.
    2. Verifica que el DPI cumpla con el formato esperado (4 dígitos, opcionalmente seguido de 5 dígitos y otros 4 dígitos).
    3. Extrae y valida el departamento y municipio según las listas definidas.
    4. Calcula y verifica el dígito verificador utilizando el algoritmo del complemento 11.
    """

    if not dpi:
        return False # En caso de que el DPI esté vacío

    dpi_regex = r'^[0-9]{4}\s?[0-9]{5}\s?[0-9]{4}$'

    if not re.match(dpi_regex, dpi):
        return False # DPI con formato inválido

    dpi = dpi.replace(' ', '')
    depto = int(dpi[9:11])
    muni = int(dpi[11:13])
    numero = dpi[0:8]
    verificador = int(dpi[8])

    # Lista de municipios por departamento
    munis_por_depto = [
        17,  # Guatemala
        8,   # El Progreso
        16,  # Sacatepéquez
        16,  # Chimaltenango
        13,  # Escuintla
        14,  # Santa Rosa
        19,  # Sololá
        8,   # Totonicapán
        24,  # Quetzaltenango
        21,  # Suchitepéquez
        9,   # Retalhuleu
        30,  # San Marcos
        32,  # Huehuetenango
        21,  # Quiché
        8,   # Baja Verapaz
        17,  # Alta Verapaz
        14,  # Petén
        5,   # Izabal
        11,  # Zacapa
        11,  # Chiquimula
        7,   # Jalapa
        17   # Jutiapa
    ]

    if depto == 0 or muni == 0:
        return False # DPI con código de municipio o departamento inválido

    if depto > len(munis_por_depto):
        return False # DPI con código de departamento inválido

    if muni > munis_por_depto[depto - 1]:
        return False # DPI con código de municipio inválido

    # Verificación del correlativo con base en el algoritmo del complemento 11
    total = 0

    for i in range(len(numero)):
        total += int(numero[i]) * (i + 2)

    modulo = total % 11

    return modulo == verificador