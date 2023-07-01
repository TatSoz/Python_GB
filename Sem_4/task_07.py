# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def companies_money(comp_dict: dict[str, list[int | float]]) -> bool:
    # is_ok = True
    #
    # for key, value in comp_dict.items():
    #     summa = sum(value)
    #     is_ok = summa > 0
    #     if not is_ok:
    #         return is_ok
    #
    # return is_ok
    return all(map(lambda el: sum(el) > 0, comp_dict.values()))


if __name__ == '__main__':
    print(companies_money({'CompA': [5_000, 6_000, -2_500], 'CompB': [5_000, 1_500, -3_500], 'CompC': [4_000, 1_000, 3_000]}))





