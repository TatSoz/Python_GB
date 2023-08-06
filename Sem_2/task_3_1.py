# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
#         Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def transl(d: int, b: int) -> str:

    l = []
    while d > 0:
        d, f = divmod(d, b)
        l.append(str(f))
    return ''.join(l[::-1])

print(transl(123, 2))
print()
print(transl(123, 8))
print('рез')
print(transl(-123, 2))
print('hp')
print(transl(-123, 8))

# print(bin(123))
print()
