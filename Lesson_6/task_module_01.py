from Lesson_6.mathematical import base_math

x = base_math.mul  # Плохой приём функция умножение имеет имя х
y = base_math._START_MULT  # Очень плохой приём импорт защищенной переменной
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)