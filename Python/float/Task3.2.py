import math

distance = float(input("Пройденное расстояние: "))
angle = math.radians(float(input("Угол поворота: ")))

x_coord = distance * math.cos(angle)
y_coord = distance * math.sin(angle)

print("Координаты нового местоположения - (", x_coord, ",", y_coord, ")")