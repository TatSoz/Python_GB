# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.

def dec_to_n(number: int, system: int) -> str:
    l = []
    while number > 0:
        number, f = divmod(number, system)
        l.append(str(f))
    return ''.join(l[::-1])







