numbers = 0
cout = 0
while numbers >= 0:
    numbers = int(input('Введите число: '))
    cout += 1
print('Найдено отрицательное число')
print('Количество чисел, без учета отрицательного:', cout - 1)