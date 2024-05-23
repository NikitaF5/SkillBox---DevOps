wallet = int(input('Сколько денег дала мама: '))
chees, icecream = 60, 20
if wallet >= 60:
    print('На сыр денег хватило!')
    wallet -= chees
    if wallet >= icecream:
        print('И на мороженное тоже!')
        wallet -= icecream
    else:
        print('Денег маловато')
else: 
    print('Денег не хватило даже на сыр!')