#encoding:utf-8

from datetime import timedelta, date, datetime
from dias import dias_semana
from festivos import dias_festivos
import csv

def rango_fechas(fecha_inicial, fecha_final):
    '''
    Genera las fechas entre fecha_inicial y fecha_final
    '''
    for n in range(int ((fecha_final - fecha_inicial).days)):
        yield fecha_inicial + timedelta(n)

def generador(fecha_inicial, fecha_final, dias, archivo):
    '''
    Genera y escribe las fechas en un archivo csv
    '''
    # Abre el archivo para escritura
    with open(archivo, 'w', newline='', encoding='utf-8') as file:
        # Obtiene el objeto que escribe en el archivo    
        writer = csv.writer(file)    

        # Escribe el encabezado
        sesion = 1
        writer.writerow(['Sesion', 'Dia', 'Fecha', 'Temas y subtemas', 'Actividades de Aprendizaje realizadas', 'Recursos didacticos empleados', 'Instrumentos de Evaluacion Aplicados'])

        # Recorre las fechas entre fecha final y fecha final
        for fecha in rango_fechas(fecha_inicial, fecha_final):

            # Obtiene el dia de la semana
            dia_semana = dias_semana[fecha.weekday()]

            # Obtiene la fecha
            fecha_sesion = fecha.strftime("%Y-%m-%d")
            
            # Verifica que se deba generar una sesion para el dia
            if dia_semana in dias:
                if fecha_sesion in dias_festivos:
                    # Escribe la fecha de la sesion como un festivo
                    writer.writerow([sesion, dia_semana, fecha_sesion, 'FESTIVO'])
                else:
                    # Escribe la fecha de la sesion
                    writer.writerow([sesion, dia_semana, fecha_sesion])

                # Incrementa la sesion
                sesion = sesion + 1

