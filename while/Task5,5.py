count, hours, score_task, count_phone = 1, 8, 0, 0

while count < hours:
    print(count, '-й час')
    task = int(input('Сколко задач решил Максим: '))
    score_task += task
    phone = int(input('Звонит жена взять трубку? 1/0: '))
    count_phone += phone
    count += 1
print('Рабочий день закончен, всего выполнено задач:', score_task)
if count_phone > 0:
    print('Нужно зайти в магазин')
    