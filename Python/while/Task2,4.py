wallet = int(input('Сколко денег: '))
while wallet < 10000:
    score_kub = int(input('Какое число выпало на кубике: '))
    if score_kub == 3:
        print('Вы проиграли все!')
        wallet = 0
        break
    else:
        print('Вы выйграли 500')
        wallet += 500
print('Итого осталось:', wallet)