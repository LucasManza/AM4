import math
from decimal import Decimal
from math import pi
import decimal


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
    i = 0
    a = Decimal(1)
    b = Decimal(1 / math.sqrt(2))
    t = Decimal(1 / 4)
    p = Decimal(1)

    while i != 4:
        a = decimal.Decimal(float(a))
        b = decimal.Decimal(float(b))
        a1 = (decimal.Decimal(a) + decimal.Decimal(b)) / decimal.Decimal('2')
        b1 = math.sqrt(a * b)
        t = t - (p * ((a - a1) ** 2))
        p = 2 * p
        a = a1
        b = b1
        i = i + 1

    result = ((decimal.Decimal(a) + decimal.Decimal(b)) ** decimal.Decimal('2')) / (decimal.Decimal('4') * decimal.Decimal(t))

    print("\nEl valor de pi es:", result)



def calcPiSpigot(max):
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while max > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and max > 0:
            yield int(d)
            max -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

def calculatePiSpigot():
    max = int(input("\nIngrese la cantidad de digitos: "))
    piSpigot = list(calcPiSpigot(max))
    result = str(list(piSpigot).pop(0))
    if max > 1:
        result += "."
    i = 1
    while i != max:
        result += str(list(piSpigot).pop(i))
        i += 1
    print(result)


selectionNumber()