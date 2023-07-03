from super_module import *  # использовать с осторожностью!

SIZE = 49.5

print(f'{SIZE = }\n{result = }')
# print(f'{z = }')  # ошибка переменная не найдета
# print(f'{_secret = }')  # ошибка переменная _secret не найдета, она не импортируется через *
print(f'{func(100, 200) = }\n{randint(10, 20) = }')


def func(a: int, b: int) -> int:
    return a + b


print(f'{func(100, 200) = }')