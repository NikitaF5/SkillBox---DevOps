count = 0
for ticket in 345, 19, 87, 1020, 421:
    if ticket >= 100 and ticket % 5 == 0:
        print(ticket, ' Выйгрышный билет')
        count += 1
    
        