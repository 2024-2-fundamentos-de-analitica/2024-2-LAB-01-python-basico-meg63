"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_11():
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in archivo:
            letras=row[3].split(",")
            suma=int(row[1])
            for letra in letras:
                if letra in diccionario.keys():
                    diccionario[letra]+=suma
                else: 
                    diccionario[letra]=suma
        return dict(sorted(diccionario.items()))
    
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
pregunta_11()