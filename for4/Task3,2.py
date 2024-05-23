x_lim = 50
y_lim = 20

delta = 3  # число 3 выбрано "на глаз", в зависимости от него дорога будет шире/уже

for y in range(y_lim):
    for x in range(x_lim):
        if y == y_lim // 2:
            print('-', end='')
        elif x == x_lim // 2:
            print('|', end='')
        elif x == x_lim // 2 - (delta + y):
            print('/', end='')
        elif x == x_lim // 2 + (delta + y):
            print('\\', end='')  # \ - символ который используется для экранирования, поэтому его пришлось дублировать
        else:
            print(' ', end='')
    print()