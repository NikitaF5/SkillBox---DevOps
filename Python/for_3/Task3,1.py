print( '-' * 10)

for i in range(4):
    for i in range(10):
        if i == 0 or i == 9:
            print('|', end = '')
        else:
            print('0', end = '')
    print('')

print( '-' * 10)