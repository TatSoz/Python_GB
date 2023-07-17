# Добавьте в пакет, созданный на семинаре, шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.


import random as rnd

# __all__ = ['check_queen', 'gen_positions']

QUEEN_COUNT: int = 8
SIZE_BOARD: int = 8


def check_queen(positions: list[tuple]) -> bool:

    result = True

    if len(positions) != QUEEN_COUNT:
        result = False
    else:
        for i in range(QUEEN_COUNT - 1):
            if not result:
                break
            row_1, col_1 = positions[i]
            count = QUEEN_COUNT
            for j in range(i + 1, count):
                row_2, col_2 = positions[j]
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break

    return result


def gen_positions() -> list[tuple[int, int]]:

    result = []
    for i in range(SIZE_BOARD):
        result.append((i, rnd.randint(0, SIZE_BOARD - 1)))
    return result

NEED_OK_POSITIONS = 4

if __name__ == "__main__":
    queens_positions = [
        [(0, 5), (1, 2), (4, 3), (2, 2), (7, 6), (5, 1), (2, 7), (3, 4)],
        [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)],
    ]

    for list_position in queens_positions:
        print(list_position)
        if check_queen(list_position):
            print("Ферзи не бьют друг друга")
        else:
            print("Ферзи под ударом")


    total_case_generate = 0
    case_ok = 0
    list_ok_positions = []

    while case_ok < NEED_OK_POSITIONS:
        generated_position = gen_positions()
        total_case_generate += 1
        if check_queen(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)

    print(f" Всего сгенерировано {total_case_generate}, успешных расстановки:")
    for pos in list_ok_positions:
        print(pos)