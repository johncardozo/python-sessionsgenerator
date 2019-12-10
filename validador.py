#encoding:utf-8

import datetime
from dias import dias_semana

def fecha_valida(fecha):
    '''
    Valida que la fecha tenga un valor con el formato YYYY-MM-DD
    '''
    # Valida que la fecha tenga valor
    if not fecha:
        return None

    # Valida que la fecha sea válida (YYYY-MM-DD)
    try:
        resultado = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
        return resultado
    except:
        return None

def fechas_coherentes(fecha_inicial, fecha_final):
    '''
    Valida que las fechas tengan valor y que la fecha inicial sea menor a la fecha final
    '''
    return fecha_inicial < fecha_final

def dias_validos(dias):
    '''
    Verifica que los días sean válidos
    '''
    # Verifica que los dias tengan un valor
    if not dias:
        return False
    # Itera sobre los dias
    for dia in dias:
        # Verifica que el dia sea válido
        if dia not in dias_semana:
            return False
    
    return True