your_xp = int(input('Введите количество опыта: '))
lvl = 1
if your_xp < 1000:
    print('Ваш уровень:', lvl)
elif your_xp >= 1000 and your_xp < 2500:
    print('Ваш уровень:', lvl + 1)
elif your_xp >= 2500 and your_xp < 5000:
    print('Ваш уровень:', lvl + 2)
else:
    print('Ваш уровень:', lvl + 3)
       