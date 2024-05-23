import math

cize = int(input('Размер файла: '))
dowload_speed = int(input('Какова скорость вашего соединения: '))
dowload = 0
time = 0

while True:
    time += 1
    dowload += dowload_speed
    percent = math.ceil((dowload * 100)/cize)
    if percent >= 100:
        print('Прошло', time, 'сек.', 'Скачано', cize, 'из', cize, 'Мб', '(100%)')
        break
    print('Прошло', time, 'сек.', 'Скачано', dowload, 'из', cize, 'Мб', '(' , percent , '%)')
    