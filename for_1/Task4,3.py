num = int(input('Какого числа ищем факториал? '))
num += 1 # Для захвата последнего числа

result = 1

for fact in range(2,num):
    result *= fact
print('Факториал числа', num - 1, 'равен:', result)