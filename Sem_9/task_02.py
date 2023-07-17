# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint
from typing import Callable

def check_parametr(func: Callable):
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT =10

    def wrapper(num: int, count: int, *args, **kwargs):
        if num > MAX_NUM or num < MIN_NUM:
            num = randint(MIN_NUM, MAX_NUM)
        if count > MAX_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)
        # print(num, count)
        result = func(num, count, *args, **kwargs)


        return result

    return wrapper


@check_parametr
def gess_number(num: int, count: int) -> Callable[[], None]:

    def gess():

        for i in range(1, count + 1):
            num_input = int(input(f'Угадайте число от 1 до 100, у Вас {count + 1 - i} попыток: '))
            print(f'Попытка № {i}')
            if num_input == num:
                print('Вы угадали!')
                break
            elif num_input < num:
                print('Загаданное число больше')
            else:
                print('Загаданное число меньше')

    return gess



if __name__ == '__main__':
    game = gess_number(125, 15)
    game()