year = int(input('Год выпуска: '))
speed = int(input('Количество скоростей: '))
if year >= 2018 and speed >= 24:
    print('Велосипед подходит!')
else:
    print('Велосипед не подходит!')