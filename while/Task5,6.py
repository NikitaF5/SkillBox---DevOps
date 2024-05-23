x = int(input('Размер вклада: '))
p = int(input('На сколько % увеличиваеться: '))
y = int(input('До какого размера должен дойти: '))
years = 0
while True:
    x = x * ((100 + p)/ 100)
    years += 1
    if x >= y:
        print('Вклад дошел до нужного размера за', years, 'лет')
        break