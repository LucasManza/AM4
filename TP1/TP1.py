import math
from decimal import Decimal
from math import pi


def selectionNumber():
    print(
        "\nPresione 1 para ver el valor de pi propuesto por la libreria de python \nPresione 2 para calcular pi con "
        "el algoritmo de Gauss-Legendre usando tipo float \nPresione 3 para calcular pi con el algoritmo de "
        "Gauss-Legendre usando tipo decimal \nPresione 4 para calcular pi con el algoritmo de Espita \nPresione 0 "
        "para salir")
    number = int(input("\nIngrese una opcion: "))

    if number == 1:
        piPython()
        selectionNumber()
    if number == 2:
        calculatePiGaussFloat()
        selectionNumber()
    if number == 3:
        calculatePiGaussDecimal()
        selectionNumber()
    if number == 4:
        calculatePiSpigot()
        selectionNumber()

def piPython():
    print("\nEl valor de pi es:", pi)

def calculatePiGaussFloat():
    i = 0
    a = float(1)
    b = float(1 / math.sqrt(2))
    t = float(1 / 4)
    p = float(1)

    while i != 4:
        a1 = (a + b) / 2
        b1 = math.sqrt(a * b)
        t = t - (p * ((a - a1) ** 2))
        p = 2 * p
        a = a1
        b = b1
        i = i + 1

    result = ((a + b) ** 2) / (4 * t)

    print("\nEl valor de pi es:", result)

def calculatePiGaussDecimal():
    print(Decimal(pi))



# Arreglar spigot, no hace lo que debe
def calculatePiSpigot():
    max = int(input("\nIngrese el numero: "))
    result = float(0)
    i = 0

    while i <= max:
        result += (math.pow(-1, i)) / ((2 * i) + 1)
        # result += (math.pow(factorial(i), 2) * math.pow(2, (i + 1)))/(factorial((2*i)+1))
        i = i + 1

#Para usar el otro algoritmo basta solo comentar lineas 58 y 63. Descomentar linea 59
    result = result * 4

    print("\nEl valor de pi es:", result)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(int(n - 1))


selectionNumber()