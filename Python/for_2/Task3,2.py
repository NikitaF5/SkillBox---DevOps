totalSoldaries = int(input('Сколько всего солдат: '))
rules_count = 1
push_up = 0
for i in range(totalSoldaries - 3, 0, -4):
    rules_count = (rules_count + i * 3) % totalSoldaries
    rules = int(input('Сколько правил: '))
    if rules != rules_count:
        print('Неправильно!', i * 10, 'отжиманий')
        push_up += i * 10
print("Всего отжиманий", push_up)