# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

X = int(input('Введите координату Х '))
Y = int(input('Введите координату Y '))

if X > 0 and Y > 0:
    print ('I четверть')
elif X < 0 and Y > 0:
    print ('II четверть')
elif X < 0 and Y < 0:
    print ('III четверть')
elif X > 0 and Y < 0:
    print ('IV четверть')
elif X == 0 and Y == 0:
    print ('В начале координат')
elif X == 0:
    print ('На оси Х')
elif Y == 0:
    print ('На оси Y')


