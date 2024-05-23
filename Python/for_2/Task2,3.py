wake_up = int(input('Во сколько проснулся: '))
sum_food, water = 0, 0
for i in range(wake_up, 23, 3):
    print('Сейчас времени', i)
    water += 1
    food = int(input('Сколко каллорий съедено: '))
    sum_food += food
print('Еды съедено:', sum_food,',а воды выпито:', water)