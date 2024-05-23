positiv = 0
negativ = 0
while True:
    n = int(input('Введите число: '))
    if n > 0:
        positiv += 1
    elif n < 0:
        negativ += 1
    else:
        break
print('Число положительных:', positiv)
print('Число отрицательных:', negativ)