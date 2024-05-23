user_weight = float(input("Вес пациента: "))
user_height = float(input("Рост пациента: "))

result = round(user_weight/user_height**2, 2)
if result < 18.5:
    print("Недобор")
elif result < 25:
    print("Норма")
elif result < 30:
    print("Избыток")
else:
    print("Ожирение")

