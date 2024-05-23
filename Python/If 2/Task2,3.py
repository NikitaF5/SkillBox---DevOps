first = int(input('Вес первой монеты: '))
second = int(input('Вес второй монеты: '))
third = int(input('Вес третей монеты: '))
if first == second:
    print('Третья легче')
elif first < second:
    print('первая легче')
else:
    print('Вторая легче')