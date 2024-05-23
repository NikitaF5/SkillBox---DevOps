phrase = input('Введите текст: ')
big_count = 0
small_count = 0

for symbol in phrase:
    if symbol == 'Ы':
        big_count += 1
    elif symbol == 'ы':
        small_count += 1
        
print('Количество больших букв Ы:', big_count)
print('Количество маленьких букв ы:', small_count)