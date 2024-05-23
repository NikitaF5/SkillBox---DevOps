n = int(input('Сколко карточек: '))

summ_card = 0

x = n + 1
fact_summ = 0
for i in range(1, x):
    fact_summ += i

for i in range(1,n):
    card = int(input('Введите номер оставшейся карточки: '))
    summ_card += card
    
num_last_card = fact_summ - summ_card
print('Потерявшееся карта под номером:', num_last_card)