from TP3.RungeKutta import rungeKutta
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

h = 0.2


def functionNewton(tm):
    return lambda x, y: (-0.25) * (y - tm)  # Retorna la funcion T'(t) = -r * (T - Tm) con su Tm correspondiente


def calculateTemperatures(temperaturesPrevious, x0, x):
    newCSV = pd.DataFrame(np.zeros(temperaturesPrevious.shape))  # Crea un array doble de 21x21 compatible con csv
    for i in range(0, 22):
        for j in range(0, 22):
            y0 = temperaturesPrevious[i][j]
            if temperaturesPrevious[i][j] == 15:  # Verifica si la casilla pertenece a la pared del horno
                newCSV[i][j] = 15
            else:
                # Si la casilla no pertenece a la pared entonces calcula su nuevo valor con runge kutta tomando como funcion a la funcion de newton
                # Se toma como Tm(temperatura del medio) a la suba de las cuatro casillas que estan en diagonal, mas cercanas a la casilla del centro, sobre 8
                # Siendo T(temperatura de la casilla) el valor que se calcula con runge kutta
                newCSV[i][j] = rungeKutta(x0, y0, h, x, functionNewton((temperaturesPrevious[i - 1][j - 1] +
                                                                        temperaturesPrevious[i - 1][j + 1] +
                                                                        temperaturesPrevious[i + 1][j - 1] +
                                                                        temperaturesPrevious[i + 1][j + 1]) / 8))
    return newCSV


def generateDATA(iterations):
    temperatures = pd.read_csv('csv/temperaturas_horno0.csv',
                               header=None)  # Pandas se encarga de que el csv se comporte como un array doble
    generateHeatMap(temperatures, 'heatMaps/temperatures_horno{}.png'.format(0), title='T{}'.format(0))
    xi = 0
    x = iterations
    for i in range(1, 11):
        temperatures = calculateTemperatures(temperatures, xi, x)  # Modifica los valores del array doble
        xi += iterations
        x += iterations
        generateCSV(temperatures, 'csv/temperatures_horno{}.csv'.format(i))
        generateHeatMap(temperatures, 'heatMaps/temperatures_horno{}.png'.format(i), title='T{}'.format(i))


def generateHeatMap(matrix, fileName, title):
    plt.clf()
    plt.title(title)
    plt.imshow(matrix, cmap='CMRmap', vmin=-5, vmax=200)
    plt.axis('off')
    plt.colorbar()
    plt.savefig(fileName)


def generateCSV(temperatures, fileName):
    temperatures.to_csv(fileName, header=False,
                        index=False)  # Crea un nuevo csv con los nuevos valores
