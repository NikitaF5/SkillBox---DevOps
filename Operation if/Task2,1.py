bank = int(input('Сколько денег на счету?'))
course_prise = 75000
if bank >= course_prise:
    print('Курс успешно преобретен!')
    bank -= course_prise
else:
    print('Не хватает денег на счете')
print('Хорошего дня!')