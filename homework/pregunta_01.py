"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework._utils import leer_datos


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum(int(fila[1]) for fila in leer_datos())
