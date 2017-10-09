import scipy
import matplotlib.pyplot as plt
import numpy as np
import csv


xAltura = [0.0] * 95
yLatitud = [0.0] * 95
yLongitud = [0.0] * 95
with open('geo_pos.csv', 'r') as f:
    line = f.read().splitlines()
    line.pop(0)
    index = 0

    altura = []  # x altura
    latitud = []  # y latitud
    longitud = []  # y longitud

    for l in line:
        linea = l.split(',')
        altura.append([float(linea[0])])
        latitud.append([float(linea[1])])
        longitud.append([float(linea[2])])

    for i in range(0, len(altura)):
        xAltura[i] = altura[i][0]
        yLatitud[i] = latitud[i][0]
        yLongitud[i] = longitud[i][0]

xAltura.reverse()
yLatitud.reverse()
yLongitud.reverse()

matrizAltitud = [None] * 19
matrizLatitud = [None] * 19
matrizLongitud = [None] * 19
for i in range(19):
    matrizAltitud[i] = [None] * 5
    matrizLatitud[i] = [None] * 5
    matrizLongitud[i] = [None] * 5

for i in range(19):
    for j in range(5):
        matrizAltitud[i][j] = xAltura[(i * 5) + j]
        matrizLatitud[i][j] = yLatitud[(i * 5) + j]
        matrizLongitud[i][j] = yLongitud[(i * 5) + j]


def polinomioLagrange(x, y):
    # Inicializar result en 0
    result = scipy.poly1d([0.0])

    for i in range(0, len(x)):
        temp_numerador = scipy.poly1d([1.0])
        denominador = 1.0

        for j in range(0, len(x)):
            if i != j:
                temp_numerador *= scipy.poly1d([1.0, -x[j]])
                denominador *= x[i] - x[j]

        result += (temp_numerador / denominador) * y[i]

    return result


polinomiosLatitud = [None] * 19   #Latitud es True
polinomiosLongitud = [None] * 19   #Longitud es False
for i in range(19):
    polinomiosLatitud[i] = polinomioLagrange(matrizAltitud[i], matrizLatitud[i])
    polinomiosLongitud[i] = polinomioLagrange(matrizAltitud[i], matrizLongitud[i])


def calculate(number, b):
    result = scipy.poly1d([0.0])
    for i in range(500, 10100, 500):
        if i >= number & i < 9500:
            if b == True :
                aux = int((i/500)-1)
                result = polinomiosLatitud[aux]
                break
            else:
                aux = int((i / 500) - 1)
                result = polinomiosLongitud[aux]
                break
        if i >= 9500:
            if b == True :
                result = polinomiosLatitud[18]
                break
            else:
                result = polinomiosLongitud[18]
                break
    return result(number)

resultLatitud = []
resultLongitud = []
resultAltura = []

for i in range(0, 10010, 10):
    resultLatitud.append(calculate(i, True))
    resultLongitud.append(calculate(i, False))
    resultAltura.append(i)


def graficarLatitud():
    x_val = np.arange(0, 10010, 10)
    plt.xlabel('Latitud')
    plt.ylabel('Altura(m)')
    plt.grid(True)

    for i in range(0, len(yLatitud)):
        plt.plot((yLatitud[i]), (xAltura[i]), 'ro')
    plt.plot(resultLatitud, x_val)
    plt.show()

def graficarLongitud():
    x_val = np.arange(0, 10010, 10)
    plt.xlabel('Longitud')
    plt.ylabel('Altura(m)')
    plt.grid(True)

    for i in range(0, len(yLongitud)):
        plt.plot((yLongitud[i]), (xAltura[i]), 'ro')
    plt.plot(resultLongitud, x_val)
    plt.show()

def graficar3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = resultLongitud
    Y = resultLatitud
    Z = resultAltura
    ax.plot_wireframe(X, Y, Z)
    plt.show()


csvLatitud = []
csvLongitud = []
csvAltura = []

for i in range(0, 10001, 1):
    csvLatitud.append(calculate(i, True))
    csvLongitud.append(calculate(i, False))
    csvAltura.append(i)

def createCSV():
    cSV = open('geoPos.csv', 'w')
    cSv = csv.writer(cSV)
    cSv.writerow(['altura', 'latitud', 'longitud'])
    while len(csvAltura) != 0:
        line = [csvAltura.pop(), csvLatitud.pop(), csvLongitud.pop()]
        cSv.writerow(line)
    cSV.close()


def main():
    print('Selecione: ')
    print('1 para graficar altura/latitud.')
    print('2 para graficar altura/longitud.')
    print('3 para graficar altura/longitud/latitud.')
    print('4 para crear un archivo .csv con los valores de latitud y longitud desde 0km hasta 10000km de altura.')
    print('0 para salir')
    number = int(input('\n'))
    if number == 1:
        graficarLatitud()
    if number == 2:
        graficarLongitud()
    if number == 3:
        graficar3D()
    if number == 4:
        createCSV()
    if number == 0:
        return
    else:
        main()

main()