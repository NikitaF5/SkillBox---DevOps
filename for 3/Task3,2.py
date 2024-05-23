first = int(input('Введите первый элемент: '))
step = int(input('Введите шаг: '))
last_sum = 0

print('\nIP адресс:', end = ' ')
for i in range(3):
    print(first, end ='.')
    last_sum += first
    first += step
print(last_sum)