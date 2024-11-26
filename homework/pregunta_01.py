"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv 
def pregunta_01():
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        suma=0
        for row in archivo:
            suma+=int(row[1])
        return suma
        
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
pregunta_01()
