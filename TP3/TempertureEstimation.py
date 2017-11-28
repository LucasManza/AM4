from TP3.CSV_Reader import readCSV
from TP3.RungeKutta import rungeKuttaOrder_4

r = 25


def functionNewton(t, tm):
    return (-r) * (t - tm)


def estimateTemperature():
    lines = readCSV('TP3/csv/temperaturas_horno.csv')

    for l in lines:
        line = l.split(',')
        for value in line:
            float(rungeKuttaOrder_4(xi,yi,h,function=functionNewton()))
    createCSV_Temperat
