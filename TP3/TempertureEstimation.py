from _pydecimal import Decimal

from TP3.RungeKutta import rungeKutta
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

h = 0.2
r = 0.25


def funcDiferential(tm):
    return lambda x, y: (-r) * (y - tm)  # Retorna la funcion T'(t) = -r * (T - Tm) con su Tm correspondiente


def calculateTempRK(tempCSV, x0, x):
    newCSV = pd.DataFrame(np.zeros(tempCSV.shape))  # Crea un array doble de 21x21 compatible con csv
    for i in range(0, 22):
        for j in range(0, 22):
            y0 = tempCSV[i][j]
            if tempCSV[i][j] == 15:  # Verifica si la casilla pertenece a la pared del horno
                newCSV[i][j] = 15
            else:
                # Si la casilla no pertenece a la pared entonces calcula su nuevo valor con runge kutta tomando como funcion a la funcion de newton
                # Se toma como Tm(temperatura del medio) a la suba de las cuatro casillas que estan en diagonal, mas cercanas a la casilla del centro, sobre 8
                # Siendo T(temperatura de la casilla) el valor que se calcula con runge kutta
                newCSV[i][j] = rungeKutta(x0, y0, h, x, funcDiferential(tm(tempCSV, i, j)))
    return newCSV


def calculateTempNewton(tempCSV, tempZero, t):
    newCSV = pd.DataFrame(np.zeros(tempCSV.shape))  # Crea un array doble de 21x21 compatible con csv
    for i in range(0, 22):
        for j in range(0, 22):
            y0 = tempCSV[i][j]
            if tempCSV[i][j] == 15:  # Verifica si la casilla pertenece a la pared del horno
                newCSV[i][j] = 15
            else:
                tmAux = tm(tempCSV, i, j)
                newCSV[i][j] = tmAux + ((tempCSV[i][j] - tmAux) * np.math.exp(-r * t))
    return newCSV


def tm(tempPrev, i, j):
    return (tempPrev[i - 1][j - 1] + tempPrev[i - 1][j] + tempPrev[i - 1][j + 1] +
            tempPrev[i][j - 1] + 0.0 + tempPrev[i][j + 1] +
            tempPrev[i + 1][j - 1] + tempPrev[i + 1][j] + tempPrev[i + 1][j + 1]) / 8.0


def generateDATA(iterations):
    tempZero = pd.read_csv('csv/temperaturas_horno0.csv',
                           header=None)  # Pandas se encarga de que el csv se comporte como un array doble
    generateHeatMap(tempZero, 'heatMaps/temperatures_horno{}.png'.format(0), title='T{}'.format(0))
    xi = 0
    x = iterations
    tempNewton = tempZero
    tempRK = tempZero
    for i in range(1, 11):
        tempRK = calculateTempRK(tempRK, i - 1, i)  # Modifica los valores del array doble
        generateCSV(tempRK, 'csv/RK_temperatures_horno{}.csv'.format(i))
        generateHeatMap(tempRK, 'heatMaps/Rk_temperatures_horno{}.png'.format(i),
                        title='RK_T{}'.format(i))
        xi += iterations
        x += iterations

        tempNewton = calculateTempNewton(tempNewton, tempZero, i)
        generateCSV(tempNewton, 'csv/Newton_temperatures_horno{}.csv'.format(i))
        generateHeatMap(tempNewton, 'heatMaps/Newton_temperatures_horno{}.png'.format(i),
                        title='Newton_T{}'.format(i))


def generateHeatMap(matrix, fileName, title):
    plt.clf()
    plt.title(title)
    # vmin and vmax for colorscale
    # cmp --> colormap. Try 'CMRmap' , 'jet', 'hot' or 'rainbow' for
    #     differents colors scale type.
    plt.imshow(matrix, cmap='jet', vmin=-5, vmax=200)
    plt.axis('off')
    plt.colorbar()
    plt.savefig(fileName)


def generateCSV(temperatures, fileName):
    temperatures.to_csv(fileName, header=False, index=False)  # Crea un nuevo csv con los nuevos valores
