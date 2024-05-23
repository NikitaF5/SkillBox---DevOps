
while True:
  print('Введите местоположение коня:')
  x = float(input(' '))
  y = float(input(' '))
  xSquare = int(x * 10)
  ySquare = int(y * 10)
 
  print('Введите местоположение точки на доске:')
  point_x = float(input(' '))
  point_y = float(input(' '))
  point_Square_X = int(point_x * 10)
  point_Square_Y = int(point_y * 10)
  
  if 0 <= xSquare <= 8 or 0 <= ySquare <= 8 or 0 <= point_Square_X <= 8 or 0 <= point_Square_Y <= 8:
    print(f'Конь в клетке ({xSquare}, {ySquare}) Точка в клетке({point_Square_X}, {point_Square_Y}).')
    break
  else:
    print('Введите координаты повторно, таких не существует!')
 
dxy = abs(xSquare - point_Square_X) + abs(ySquare - point_Square_Y) == 3 
if dxy:
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')