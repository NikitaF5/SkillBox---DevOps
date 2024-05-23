answer = 'Пушкин'
bad_count = 0
for i in range(0, 5):
    who = input('Кто написал произвидение? ')
    if who == answer:
        print('Правильно!')
        break
    print('Неправильно! Два!')
    bad_count += 1