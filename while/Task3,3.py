blok = 1
while blok:
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    kod = int(input('Введите код: '))
    if kod == 235:
        print('Код верный, завершаю работу... ')
        blok = 0
    