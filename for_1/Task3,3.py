wake_up = int(input('Во сколько проснулся: '))
sum_calories = 0
awake_hours = 0

for hour in range(wake_up, 23):
    print('Сейчас часов:', hour)
    calories = int(input('Сколько сьел калорий за час: '))
    sum_calories += calories
    if sum_calories > 2000:
        print('Лимит калорий... Пора спать')
        break
    awake_hours += 1
print('Сегодня съедено каллорий: ', sum_calories)
print('Часов не спал:', awake_hours)