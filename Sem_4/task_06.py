# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.


def number_sum(num_list: list[int | float], index_1: int, index_2: int) -> int | float:
    index_max = max(index_1, index_2) + 1 if max(index_1, index_2) + 1 < len(num_list) else len(num_list)
    index_min = min(index_1, index_2) if min(index_1, index_2) >= 0 else 0

    return sum(num_list[index_min:index_max])


if __name__ == '__main__':
    print(number_sum([1, 3, 6, 4, 8, 0, 3], 4, 1))











