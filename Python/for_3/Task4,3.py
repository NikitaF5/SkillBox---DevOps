rows = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений в ряде: '))
meters = int(input('Введите кол-во метров между рядами: '))

for i in range(rows):
    for i in range(seats):
        print('=' * seats, end = '')
        for i in range(meters):
            print('', end = ' ')
            print('*' * meters, end = '')
            print('', end = ' ')
            break
        print('=' * seats, end = '')
        print('')
        break