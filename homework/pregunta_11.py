"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import defaultdict

from homework._utils import leer_datos, parsear_c4


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    acumulado = defaultdict(int)
    for fila in leer_datos():
        for letra in parsear_c4(fila[3]):
            acumulado[letra] += int(fila[1])
    return dict(sorted(acumulado.items()))
