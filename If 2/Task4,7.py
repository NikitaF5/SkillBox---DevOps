time = int(input('Время: '))
if (time >= 8 and time <= 22) and (time <= 14 or time >= 15) and (time <= 10 or time >= 12) and (time <= 18 or time >= 20):
    print('Посылку можно получить!')
else:
    print('Посылку получить нельзя!')