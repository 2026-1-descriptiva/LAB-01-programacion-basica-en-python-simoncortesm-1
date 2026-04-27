import csv


def leer_datos():
    with open("files/input/data.csv", encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        return [fila for fila in lector]


def parsear_c4(campo):
    return campo.split(",")


def parsear_c5(campo):
    pares = []
    for item in campo.split(","):
        clave, valor = item.split(":")
        pares.append((clave, int(valor)))
    return pares
