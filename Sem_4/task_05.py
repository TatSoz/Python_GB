# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
import decimal


def money(names_list: list[str], staff_list: list[int], bonus_list: list[str]) -> dict[str, decimal.Decimal]:
    money_dict = dict()
    # for i in range(len(names_list)):
    #     money_dict[names_list[i]] = staff_list[i] * decimal.Decimal(bonus_list[i][:-1]) / 100

    for name, staff, bonus in zip(names_list, staff_list, bonus_list):
        money_dict[name] = staff * decimal.Decimal(bonus[:-1]) / 100

    return money_dict


if __name__ == '__main__':
    print(money(['Иван', 'Андрей', 'Дмитрий'], [50_000, 35_000, 75_000], ['15.25%', '20.50%', '8.55%']))



