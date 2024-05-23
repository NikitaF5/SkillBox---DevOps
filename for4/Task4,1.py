human_count = int(input("Введите количество людей в очередь: "))
for human_start in range(human_count + 1):
    print("Прошло часов:", human_start)
    for human_number in range(human_start, human_count):
        print('Номер в очереди', human_number,)
    print()
print('Очеред обслужена!')