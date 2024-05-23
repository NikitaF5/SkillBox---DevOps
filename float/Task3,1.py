import math

a = float(input("Введите сторону а: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2

area_formula = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Площадь треугольника:", area_formula)