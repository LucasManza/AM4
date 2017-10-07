
# No logro que el algoritmo tome los datos de las listas para armar los resultados



# Open() recibe el archivo csv y los datos los coloca en 3 arrays
altura = []
latitud = []
longitud = []

with open('geo_pos.csv', 'r') as f:
    line = f.read().splitlines()
    line.pop(0)

    for l in line:
        linea = l.split(',')
        altura.append([float(linea[0])])
        latitud.append([float(linea[1])])
        longitud.append([float(linea[2])])




# Algoritmo de Newton
print ("------- Interpolacion Polinomica (Newton) -------")
n = int(94)+1

matriz = [0.0] * n
for i in range(n):
    matriz[i] = [0.0] * n

vector = [0.0] * n

for i in range(n):
    x = input("Ingrese el valor de x: ")
    y = input("Ingrese el valor de f("+x+"): ")
    vector[i] = float(x)
    matriz[i][0] = float(y)
    # x = altura.pop()
    # y = latitud.pop()
    # vector[i]=float(x[0])
    # matriz[i][0]=float(y[0])


punto_a_evaluar = float(input("Ingrese el punto a evaluar: "))

print ("------------------------------")
print ("------- Calculando ... -------")
print ("------------------------------")

for i in range(1,n):
    for j in range(i,n):
        matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vector[j]-vector[j-i]))

aprx = 0
mul = 1.0
for i in range(n):
    mul = matriz[i][i];
    for j in range(1,i+1):
        mul = mul * (punto_a_evaluar - vector[j-1])
    aprx = aprx + mul

print ("El valor aproximado de f(",punto_a_evaluar,") es: ", aprx)