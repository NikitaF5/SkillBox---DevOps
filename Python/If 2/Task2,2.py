wallet = int(input('Сколько ты зарабатываешь: '))
if wallet <= 0:
    print('Ошибка, доход не может быть отрицательным')
elif wallet <= 10000:
    print('Налог равен:', wallet * 0.13)
elif wallet <= 50000:
    print('Налог равен:', wallet * 0.2)
else:
    print('Налог равен:', wallet * 0.3)