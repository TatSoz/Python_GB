# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
from random import randint
from typing import Callable
import os


def generating_csv_file(file_name: str):
    MIN_ROWS = 100
    MAX_ROWS = 1001
    MIN_NUMBER = 0
    MAX_NUMBER = 100

    rows = []
    for _ in range(randint(MIN_ROWS, MAX_ROWS)):
        a, b, c = random.sample(range(MIN_NUMBER, MAX_NUMBER), 3)
        rows.append([a, b, c])
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_wr = csv.writer(f)
        csv_wr.writerow(['a', 'b', 'c'])
        csv_wr.writerows(rows)


def data_from_csv_wrap(file_name: str):
    def deco(func: Callable):
        results = []
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8', newline='') as c:
                csv_reader = csv.reader(c)
                for i, line in enumerate(csv_reader):
                    if i:
                        results.append(func(*map(int, line), **kwargs))
            return results

        return wrapper

    return deco


def save_results_to_json(func: Callable):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as j:
            result_list = json.load(j)
    else:
        result_list = []

    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'(a, b, c)': args,
                  'result': func_res}
        result_list.append(result)
        with open(file_name, "w", encoding="utf-8") as j:
            json.dump(result_list, j, indent=2)
        return func_res

    return wrapper


@data_from_csv_wrap('random.csv')
@save_results_to_json
def quadratic_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d < 0:
        x_1 = x_2 = 'None'
    elif a == 0:
        x_1, x_2 = -c / b, 'None'
    elif d == 0:
        x_1, x_2 = -b / 2 * a, 'None'
    else:
        x_1, x_2 = (-b + d ** .5) / (2 * a), (-b - d ** .5) / (2 * a)
    return x_1, x_2



if __name__ == "__main__":
    generating_csv_file('random.csv')
    quadratic_equation()
