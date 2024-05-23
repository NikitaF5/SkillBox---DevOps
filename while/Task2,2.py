numbers = int(input('Введите число: '))
summ_num = 0
while numbers != 0:
    last_num = numbers % 10
    if last_num == 5:
        print('Обнаружен разрыв!')
        break
    summ_num += last_num
    numbers //= 10
print(summ_num)