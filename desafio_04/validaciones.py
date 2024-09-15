import re

def validadr_id_unico(matriz,id):
    """
    Verifica si el ID del estudiante ya existe en la matriz.
    """
    
    for estudiante in matriz:
        if estudiante[0] == id:
            return 0 # ID ya existe
    return 1 #ID es único
    
def validar_promedio(promedio):
    """
    Verifica si el promedio está entre 1 y 10
    Devuelve 1 si el promedio es válido, 0 si no lo es.
    """
    return 1 if 1 <= promedio <= 10 else 0

def validar_correo(correo):
    '''
    Valida el formato del correo electrónico utilizando un expresión regular
    '''

    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, correo):
        return 1
    return 0

def validar_telefono(telefono):
    '''
    Valida el formato del número de telefono
    utiliza expresiones regulares para verificar el formato
    retorna 1 si el formato es válido y 0 si no lo es.
    '''

    patron = r'^\d{3} \d{4}-\d{4}$'

    if re.match(patron, telefono):
        return 1
    return 0


def validar_codigo_postal(codigo_postal):
    '''
    Valida el formato del código postal del estudiante
    utiliza expresiones regulares para verificar el formato
    '''

    patron = r'^([A-Za-z]\d{4}[A-Zaz]{3})'

    if re.match(patron,codigo_postal):
        return 1
    return 0

def validar_fecha(fecha):
    """
    Verifica si la fecha está en el formato 'YYYY-MM-DD' mediante el uso de expresiones regulares.
    """
    # Expresión regular para verificar el formato de fecha
    patron = r'^\d{2}-\d{2}-\d{4}$'
    if re.match(patron, fecha):
        # La fecha se encuentra en el formato correcto
        return 1
    else:
        # La fecha no se encuentra en el formato correcto
        return 0
    




