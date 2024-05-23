chatles = int(input("Сколько чатлов? "))
cr_convert_coef = 1 / 2200
cr_out = chatles * cr_convert_coef
print("Это", cr_out, "CR")
ship_price = 0.5
ships_can_buy = int(cr_out / ship_price)
print("Можно купить кораблей:", ships_can_buy)
