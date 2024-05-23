sum_price = 0
for mouth in range(1,13):
    print('Сейчас', mouth, 'месяц')
    price = int(input('Введите вашу зарплату за месяц: '))
    sum_price += price
result = sum_price/12
print('Средняя зарплата за год', result)