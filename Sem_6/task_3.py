"""Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""


from sys import argv
from random import randint as rint
def guess_number(min_num: int, max_num: int, counts :int) -> bool:
    number = rint(min_num, max_num)

    for _ in range(counts):
        current_num = int(input(f'Введите число от {min_num} до {max_num}: '))
        if current_num < number:
            print('Искомое число больше этого')
        elif current_num > number:
            print('Искомое число меньше этого')
        else:
            print('Вы угадали!')
            return True

    print(f"Попытки кончились, Вы не угодали число {number}")
    return False

if __name__ == "__main__":
    x = (int(i) for i in argv[1:])
    guess_number(*x)



