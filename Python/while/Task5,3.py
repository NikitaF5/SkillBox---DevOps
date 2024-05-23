num = int(input('Начальное число: '))
count = 0
while num > 0:
    count += 1
    num //= 10
print('всего чисел =', count)