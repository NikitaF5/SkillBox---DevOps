text = input('Введите текст: ')
count = 0

for i in text:
    count += 1
    if i == '*':
        print('* стоит на', count, 'месте')
        break