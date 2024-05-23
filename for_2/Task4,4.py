a = int(input('Начальная точка: '))
b = int(input('Конечная точка: '))
c = int(input('На что должно быть кратно: '))
total, count = 0, 0
for i in range(a, b+1):
    print(i)
    if i % c == 0:
        total += i
        count += 1
print('Среднее арифметическое:', total/count)