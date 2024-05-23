for i in range(10, 100):
    one = i // 10
    two = i % 10
    if i == 3 * (one * two):
        print('Число', i, 'подходит по условию')
        