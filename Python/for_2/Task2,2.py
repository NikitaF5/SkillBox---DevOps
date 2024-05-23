n = int(input('Сколько стульев: '))
char_sum = 0
for i in range(1, n, 5):
    print('Номер стула:', i)
    char_sum += i
print(char_sum)