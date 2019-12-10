#encoding:utf-8

# modulos
import argparse
from validador import fecha_valida, fechas_coherentes, dias_validos
from generador import generador

# Inicializa el parser
parser = argparse.ArgumentParser()

# Agrega los argumentos requeridos
parser.add_argument('--archivo', '-a', help='Archivo CSV. Uso: -f archivo.csv')
parser.add_argument('--fecha_inicial', '-fi', help='Fecha inicial de clase. Uso: -ff 2018-08-30')
parser.add_argument('--fecha_final', '-ff', help='Fecha final de clase. Uso: -ff 2018-08-30')
parser.add_argument('--dias', '-d', nargs='+', help='Dias de las sesiones. Uso: -d LU MA MI JU VI SA')

# Lee los argumentos de la linea de comandos
args = parser.parse_args()
fecha_inicial = args.fecha_inicial
fecha_final = args.fecha_final
dias = args.dias
archivo = args.archivo

# Obtiene las fechas
fi = fecha_valida(fecha_inicial)
ff = fecha_valida(fecha_final)

# Verifica los argumentos
if not archivo:
    print('Falta el parámetro --archivo')
if not fi:
    print('Falta el parámetro --fecha_inicial o tiene formato incorrecto (YYYY-DD-MM)')
elif not ff:
    print('Falta el parámetro --fecha_final o tiene formato incorrecto (YYYY-DD-MM)')
elif not fechas_coherentes(fi, ff):
    print(f'La fecha inicial ({fi}) debe ser anterior a la fecha final ({ff})')
elif not dias_validos(dias):
    print('Falta el parámetro de días o no son válidos')
else:
    # Mensaje para el usuario
    print('Todos los argumentos son válidos')
    print(f'Generando las sesiones para los días {dias} entre las fechas {fecha_inicial} y {fecha_final}...')

    # Genera el archivo con las sesiones
    generador(fi, ff, dias, archivo)

    print(f'Se generó el archivo {archivo} exitosamente!')

