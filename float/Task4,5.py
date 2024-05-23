import math

radius = float(input('Введите радиус планеты: '))
a = 10.8321 * (10 ** 11)
a1 = round(4 * math.pi / 3 * (radius ** 3), 3)
answer = 'Объём планеты Земля {0} в {1} раз.'

if a1 < a:
    print(answer.format('больше', round(a / a1, 3)))
else:
    print(answer.format('меньше', round(a1 / a, 3)))