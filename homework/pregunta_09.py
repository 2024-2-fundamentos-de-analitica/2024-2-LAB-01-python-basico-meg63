"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_09():
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in archivo:
            claves=row[4].split(",")
            for clave in claves:
                codigo=clave.split(":")
                if codigo[0] in diccionario.keys():
                    diccionario[codigo[0]]+=1
                else:
                    diccionario[codigo[0]]=1
        diccionario=dict(sorted(diccionario.items()))
        return diccionario
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
pregunta_09()