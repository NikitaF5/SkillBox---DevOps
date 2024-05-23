user_age = int(input("Ваш возраст? "))
user_temperature = float(input("Ваша температура тела? "))

formula_for_money = user_age * 1.5 * user_temperature
print(round(formula_for_money, 2))