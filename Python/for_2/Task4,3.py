reverse_timer = int(input('Сколько секунд греть: '))
for i in range(reverse_timer, 0, -1):
    print(i, 'секунда')
    n = int(input('Готовы забрать еду? 1/0: '))
    if n == 1:
        print('Ваша еда готова, можете забрать')
        print('Отчет закончен на', i, 'секунде')
        break