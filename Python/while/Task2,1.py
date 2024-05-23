temp = int(input('Сколько градусов на улице: '))
distance = 0
while temp > 15:
    distance += 20
    temp -= 2
    if temp < 15:
        break
    distance += 10
print('Прошли:', distance)