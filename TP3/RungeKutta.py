def rungeKuttaOrder_4(xi, yi, h, function):
    k1 = function(xi, yi)
    k2 = function(xi + (h / 2), yi + (k1 * (h / 2)))
    k3 = function(xi + (h / 2), yi + (k2 * (h / 2)))
    k4 = function(xi + h, yi + (k3 * h))
    return yi + ((h / 6) * (k1 + k2 + k3 + k4))
