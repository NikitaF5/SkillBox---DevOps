n = int(input('Сколько раз перетаскивали рыбу? '))
count = 0
fish_weight = 0

while count < n:
    fish_weight += int(input('Вес мешка: '))
    count += 1

print('Суммарный вес рыбы', fish_weight)