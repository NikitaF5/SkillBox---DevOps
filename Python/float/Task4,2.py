import math

num = float(input('Введите число: '))
result = 0

if num >= 0:
    num = math.ceil(num)
    result = math.log2(num)
    print('x =', num, '2log(x) =', result)
elif num < 0:
    num = math.floor(num)
    result = math.exp(num)
    print('x =', num, 'exp(x) =', result)
    