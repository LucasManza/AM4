import scipy
import matplotlib.pyplot as plt
import numpy as np


# Codigo para conseguir los datos del excel
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

    for i in range(1, len(altura)):
        xAltura[i] = altura[i][0]
        yLatitud[i] = latitud[i][0]
        yLongitud[i] = longitud[i][0]


xAltura.reverse()
yLatitud.reverse()
yLongitud.reverse()





# Codigo para calcular el polinomio por Lagrange
result = scipy.poly1d([0.0])

for i in range(0, len(xAltura)):
    temp_numerador = scipy.poly1d([1.0])
    denominador = 1.0

    for j in range(0, len(xAltura)):
        if i != j:
            temp_numerador *= scipy.poly1d([1.0, -xAltura[j]])
            denominador *= xAltura[i] - xAltura[j]

    result += (temp_numerador / denominador) * yLatitud[i]

print('El polinomio es: ')
print(result)
print('')






# Codigo para el grafico
x_val = np.arange(min(xAltura), max(xAltura) + 1, 1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

for i in range(0, len(xAltura)):
    plt.plot((yLatitud[i]), (xAltura[i]), 'ro')
plt.plot(result(x_val), x_val)
plt.show()