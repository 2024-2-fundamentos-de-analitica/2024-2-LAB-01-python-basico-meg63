"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
     with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in archivo:
            if row[0] in diccionario.keys():
                diccionario[row[0]].append(int(row[1]))
            else:
                diccionario[row[0]] = [int(row[1])]
        respuesta=[]
        for clave in diccionario:
            respuesta.append((clave,max(diccionario[clave]),min(diccionario[clave])))
        return sorted(respuesta)
        """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
print(pregunta_05())