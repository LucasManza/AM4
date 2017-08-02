from math import pi


def selectionNumber():
    print("\nPresione 1 para ver el valor de pi propuesto por la libreria de python \nPresione 2 para calcular pi con el algoritmo de Gauss-Legendre usando tipo float \nPresione 3 para calcular pi con el algoritmo de Gauss-Legendre usando tipo decimal \nPresione 4 para calcular pi con el algoritmo de Espita \nPresione 0 para salir")
    number = int(input("\nIngrese el numero: "))

    if number == 1:
        piPython()
        selectionNumber()
    if number == 2:
        selectionNumber()
    if number == 3:
        selectionNumber()
    if number == 4:
        selectionNumber()

def piPython():
    print("\nEl valor de pi es:", pi)


selectionNumber()