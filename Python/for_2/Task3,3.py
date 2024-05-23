n = int(input('До какого числа: '))
even_n = n -n % 2
for i in range(even_n, 0, -2):
    print(i)
print('Я иду искать!')