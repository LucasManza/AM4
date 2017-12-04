from TP3.TempertureEstimation import generateDATA


def options():
    print('Select: ')
    print('1 Simulate Temperatures: 1 iteration')
    print('2 Simulate Temperatures: 5 iteration')
    print('3 Simulate Temperatures: 10 iteration')
    print('4 Simulate Temperatures: 100 iteration')
    print('0 Exit')
    number = int(input('\n'))
    if number == 1:
        print('Analyzing...')
        generateDATA(1)
    if number == 2:
        print('Analyzing...')
        generateDATA(5)
    if number == 3:
        print('Analyzing...')
        generateDATA(10)
    if number == 4:
        print('Analyzing...')
        generateDATA(100)
    if number == 0:
        return
    else:
        options()

if __name__ == '__main__':
    options()