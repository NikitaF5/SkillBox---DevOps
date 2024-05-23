first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print('Все числа совпадают!')
elif (first == second and first != third) or (second == third and second != first):
    print('Два числа совпадают!')
else:
    print('Нет совпадений!')
