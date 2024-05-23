matem = int(input('Балл по математике: '))
himia = int(input('Балл по химии: '))
russ = int(input('Балл по русскому: '))
summ = matem + himia + russ
if summ > 270:
    print('Поздравляю вы прошли на бюджет!')
else:
    print('К сожалению, вы не прошли на бюджет')
print('Всего доброго!')