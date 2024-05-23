n = int(input('Сколко должников: '))
total_dolg = 0
for i in range(0, n, 5):
    print('Должник с номером', i)
    dolg = int(input('Сколько должны? '))
    total_dolg += dolg
print('Общая сумма долга', total_dolg)