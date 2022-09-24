# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input("Enter X for the first point: "))
y1 = int(input("Enter Y for the first point: "))
x2 = int(input("Enter X for the second point: "))
y2 = int(input("Enter Y for the second point: "))

distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

print(f'{distance = :.2f}')