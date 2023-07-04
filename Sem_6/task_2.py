# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as rint

def guess_number(min_num: int, max_num: int, counts:int) -> bool:
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


if __name__ == '__main__':
    guess_number(0, 100, 10)


