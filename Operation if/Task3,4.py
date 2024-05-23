a = int(input('Цена первого стула: '))
b = int(input('Цена второго стула: '))
c = int(input('Цена третьего стула: '))
itog = a + b + c
if itog > 10000:
    itog -= (itog * 10 / 100)
    print('Итоговая сумма', itog)
else:
    print('Итоговая сумма', itog)