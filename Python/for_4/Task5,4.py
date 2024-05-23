n = int(input('Введите количество чисел: '))
count = 0

for i in range(n):
    number = int(input('Введите число: '))
    if number % number == 0 and number % 1 == 0 and number % 2 != 0:
        count += 1
print('Количество простых чисел:', count)