def lagrange(numbersOfElements, x, i, listX):
    result = float(0)
    for j in range(0, numbersOfElements):
        if j != i:
            result *= float((x - listX[j]) / (listX[i] - listX[j]))
        return result


# Basta solo con evaluar el polinomio en ese punto x y te devuelve el valor en x resultante.
def polynomial(numbersOfElements, x, listX, listY):
    result = float(0)
    for i in range(0, numbersOfElements):
        result += ( (lagrange(numbersOfElements, x, i, listX) * listY[i]) )
    return result

numbersX = [1,3,5,7,9]
numbersY = [2,4,6,8,10]

print(polynomial(len(numbersX), 2, numbersX, numbersY))