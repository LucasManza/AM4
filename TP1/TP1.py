import math
from math import pi


def selectionNumber():
    print("\nPresione 1 para ver el valor de pi propuesto por la libreria de python \nPresione 2 para calcular pi con el algoritmo de Gauss-Legendre usando tipo float \nPresione 3 para calcular pi con el algoritmo de Gauss-Legendre usando tipo decimal \nPresione 4 para calcular pi con el algoritmo de Espita \nPresione 0 para salir")
    number = int(input("\nIngrese el numero: "))

    if number == 1:
        piPython()
        selectionNumber()
    if number == 2:
        calculatePiGaussFloat()
        selectionNumber()
    if number == 3:
        selectionNumber()
    if number == 4:
        calculatePiSpigot()
        selectionNumber()

def piPython():
    print("\nEl valor de pi es:", pi)

def calculatePiGaussFloat():
    i=0
    a = float(1)
    b = float(1/math.sqrt(2))
    t = float(1/4)
    p = float(1)

    while i != 4:
        a1 = (a+b)/2
        b1 = math.sqrt(a*b)
        t = t - (p*((a-a1)**2))
        p = 2*p
        a=a1
        b=b1
        i=i+1

    result = ((a+b)**2)/(4*t)

    print("\nEl valor de pi es:", result)



# Arreglar spigot, no hace lo que debe
def calculatePiSpigot():
    max = int(input("\nIngrese el numero: "))
    result = float(0)
    i=0

    while i != max:
        result = result + float(((-1)**i)/((2*i)+1))
        i = i+1

    result = result*4

    print("\nEl valor de pi es:", result)


selectionNumber()