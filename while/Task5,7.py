n = int(input('Какое число загадали: '))
num = 0
count = 0
while num != n:
    num = int(input('Введите число: '))
    if num > n:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        count += 1
    elif num < n:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        count += 1
print('Вы угадали! Число попыток:', count)