hours = int(input('Количество отработаных часов: '))
kredit = int(input('Отсаток по кредиту: '))
food_prise = int(input('Расходы на еду: '))
ganarar = ((200 * hours)/(2 ** 3)) + hours
if ganarar >= kredit + food_prise:
    print('Часов хватает, можно отдохнуть')
else:
    print('Часов не хватает, нужно работать больше!')