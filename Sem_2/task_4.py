# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.


import decimal
import math

PI = decimal.Decimal(math.pi)
decimal.getcontext().prec = 42
diameter = decimal.Decimal(input('Введите диаметр круга не более 1000 у.е.: '))

if diameter <= 1000:
    print(f'Площадь круга с диаметром {diameter} = {PI * diameter ** 2 / 4}')
    print(f'Длина окружности с диаметром {diameter} = {PI * diameter}')
else:
    print('Димаметр не может превышать 1000')
