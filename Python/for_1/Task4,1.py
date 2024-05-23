for x in range(10):
    numbers = int(input('Введите число: '))
    if numbers % 2 == 0 and numbers > 0:
        print('Число', numbers, 'подходит')
    else:
        print('Число не подходит по условию')