cost = int(input('Стоимость квартиры: '))
size = int(input('Размер кваритры: '))
if size > 100 and not cost > 10:
    print('Квартиру попросторнее!')
elif size >= 80 and not cost > 7:
    print('Квартиру поменьше!')