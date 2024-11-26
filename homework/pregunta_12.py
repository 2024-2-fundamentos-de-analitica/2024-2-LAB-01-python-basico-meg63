"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_12():
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in archivo:
            valores=row[4].split(",")
            suma=0
            for valor in valores:
                valor=valor.split(":")
                suma+=int(valor[1])

            if row[0] in diccionario.keys():
                diccionario[row[0]]+=suma
            else:
                diccionario[row[0]] = suma

        return dict(sorted(diccionario.items()))
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
pregunta_12()