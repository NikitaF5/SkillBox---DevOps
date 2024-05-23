gamer = int(input('Число игрока: '))
owner = int(input('Число владельца: '))
if gamer >= owner:
    print('Разность', gamer - owner)
    print('Игрок платит')
else:
    print('Разность', gamer - owner)
    print('Владелец платит')
print('Конец игры!')