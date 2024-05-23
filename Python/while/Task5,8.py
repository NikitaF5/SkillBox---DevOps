n = int(input('Какоче число загадно: '))
count = 0
start = 1
finish = 100
x = 0
while True:
    x = (start + finish) // 2
    print('Твоё число равно, меньше или больше, чем число', x, '?')
    answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
    if answer == 1:
        print('Я угадал! Спасибо за игру.')
        break
    elif answer == 2:
        start = x
    elif answer == 3:
        finish = x
print(count)