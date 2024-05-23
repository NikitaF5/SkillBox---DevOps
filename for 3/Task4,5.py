text = input('Введите текст: ')
count = 0
log = 0

for i in text:
    if i != ' ':
        count += 1
    elif i == ' ':
        if count > log:
            log = count
        count = 0
        
print('Максимальная длина слова', log, 'букв')