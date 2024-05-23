x_lim = 30
y_lim = 20

for y in range(y_lim):
    for x in range(x_lim):
        if y == 0:
            print('-', end='')
        elif x == 0 or x == x_lim - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()