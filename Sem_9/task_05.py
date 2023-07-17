# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from typing import Callable
from random import randint
import os
import json

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

def logger(func: Callable):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        json_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1)

        return result

    return wrapper


def count_f(num: int = 1):
    def deco(func: Callable):
        results = []
        def wrapper(*args, **kwargs):
            for i in range(num):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return deco


@count_f(2)
@check_parametr
@logger
def gess_number(num: int, count: int) -> Callable[[], None]:

    for i in range(1, count + 1):
        num_input = int(input(f'Угадайте число от 1 до 100, у Вас {count + 1 - i} попыток: '))
        print(f'Попытка № {i}')
        if num_input == num:
            return 'Вы угадали!'
        elif num_input < num:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')

    return 'Вы не угадали!'



if __name__ == '__main__':
    game = gess_number(25, 5)
    print(game)

