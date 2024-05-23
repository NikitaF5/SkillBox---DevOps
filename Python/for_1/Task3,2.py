first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

second += 1 # + 1 чтобы учитывалос последнее число
summ = 0 

for num in range(first,second):
    summ += num
    print(summ)