scores = int(input('Количество баллов ЕГЭ: '))
medals = int(input('Есть медали или нет? '))
if scores >= 280 and medals == 1:
    print('Поздравляем ты поступил!')
else:
    print('Не хватило баллов')