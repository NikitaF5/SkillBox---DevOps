text = input('Введите строку: ')
milk = 0
stoilo = 0

for i in text:
    stoilo += 2
    if i == 'b':
        milk += stoilo
        
print(milk)
            