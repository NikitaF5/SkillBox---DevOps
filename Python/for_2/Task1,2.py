total_hours = int(input('Сколько часов: '))
ameba_count = 1

for i in range(1, total_hours//3 + 1):
    ameba_count *= 2
    print('Прошло часов:', i * 3)
    print('Клеток:', ameba_count)
    print('Часов до конца эксеремента', total_hours - i * 3)
print('Наблюдение завершено!')