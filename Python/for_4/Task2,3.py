x_lim = 50
y_lim = 20

for y in range(y_lim):
    for x in range(x_lim):
        if y == y_lim // 2:
            print('-', end='')
        elif x == x_lim // 2:
            print('|', end='')
        else:
            print(' ', end='')
    print()