a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

summ = 0
for i in range(a,b):
    if i % 3 == 0:
        summ += i
result = summ/(b - a)
print('Среднее арифметическое в отрезке:', result)