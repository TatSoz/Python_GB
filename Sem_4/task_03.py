# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def symbol_number(num_text: str) -> dict[str, int]:
    num_1, num_2 = map(int, num_text.split())
    num_dict = dict()
    for i in range(min(num_1, num_2), max(num_1, num_2) + 1):
        num_dict[chr(i)] = i

    return num_dict

if __name__ == '__main__':
    txt = input('Введите два числа через пробел: ')
    print(symbol_number(txt))


# Вариант 2

# def create_char_dict(start, end):
#     return {chr(i): i for i in range(start, end +1)}
#
#
# num_start, num_end = sorted(map(int, input('Введите два числа через пробел: ').split()))
# print(create_char_dict(num_start, num_end))

