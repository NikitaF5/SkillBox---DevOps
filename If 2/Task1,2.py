bank = int(input('Количество денег на счету: '))
course_prise = 75000
if bank >= course_prise:
    print('Курс успешно преобретен!')
    bank -= course_prise
    print('Остаток на счете:', bank)
    if bank < 5000:
        bank += 1000
        print('Сделана скидка')
else:
    print('На счете не достаточно средств')
print('Хорошего дня!')