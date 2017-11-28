import csv


def readCSV(path):
    csv_FileReader = open(path, 'r')
    lines = csv_FileReader.read().splitlines()
    return lines



def createCSV_Temperature(path, lines):
    csv_file = open(path, 'w')
    cSv = csv.writer(csv_file)

    for l in lines:
        line = l.split(',')
        for value in line:
            cSv.writerow

    cSv.writerow(['altura', 'latitud', 'longitud'])
    while len(csvAltura) != 0:
        line = [csvAltura.pop(), csvLatitud.pop(), csvLongitud.pop()]
        cSv.writerow(line)


    csv_file.close()