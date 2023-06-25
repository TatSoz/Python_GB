# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
#         Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def input_n():
    system: int = 0
    while system not in (2, 8):
        system = int(input(f'В какую систему счисления перевести число?\n'
                           f'Двоичная - введите "2"\n'
                           f'Восьмеричная - введите "8"'))
    return system


def dec_to_n(number: int, system: int) -> str:
    tmp_num: int = number
    new_num: str = ''

    while tmp_num != 0:
        mod: str = str(tmp_num % system)
        new_num = mod + new_num
        tmp_num //= system

    return new_num


if __name__ == '__main__':
    num = int(input('Введите целое число... '))
    num2: str = dec_to_n(num, input_n())
    print(num2)
    print(f'Это число в двоичном представлении - {bin(num)}')
    print(f'Это число в восьмеричном представлении - {oct(num)}')
    print(f'Это число в десятичном представлении - {int(num2, base=2)}')


