n = int(input('Введите стипендию: '))
count = 0
for i in range(1, 11):
    prise = int(input('месячные траты '))
    print('В', i, 'месяц траты', prise, 'не хватает', prise - n)
    count += prise - n
print('Нужно пропросить у родителей', count, 'рублей')