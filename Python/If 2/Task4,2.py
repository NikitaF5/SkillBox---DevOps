x = int(input('Введите X: '))
if x > 0:
    y = x - 12
    print('Y =', y)
elif x == 0:
    y = 5
    print('Y =', y)
elif x < 0:
    y = x ** 2
    print('Y =', y)