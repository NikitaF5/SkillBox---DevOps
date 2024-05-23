three, four, five = 0, 0, 0
for i in range(12):
    print('Ученик номер', i + 1)
    n = int(input('Какая оценка? 3/4/5: '))
    if n == 3:
        three += 1
    elif n == 4:
        four += 1
    elif n == 5:
        five += 1
if three > four:
    if three > five:
        print('Большего всего троешников')
    else:
        print('Больше всего отличников')
elif four > five:
    print('Болше всего хорошистов')
