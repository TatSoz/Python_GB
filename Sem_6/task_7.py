"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
MIN_DATE = 1
MAX_YEAR = 9999
MAX_MONTH = 12
MAX_DAY = 31

__all__ = ['is_real_date']


def is_real_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if not(MIN_DATE <= year <= MAX_YEAR and MIN_DATE <= month <= MAX_MONTH and MIN_DATE <= day <= MAX_DAY):
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and _is_leap_year(year) and day > 29:
        return False

    if month == 2 and not _is_leap_year(year) and day > 28:
        return False

    return True


def _is_leap_year(year: int) -> bool:
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


if __name__ == '__main__':
    print(is_real_date('03.07.2023'))
    print(is_real_date('13.07.2023'))
    print(is_real_date('03.15.2023'))
    print(is_real_date('03.02.-2022'))
    print(is_real_date('00.15.2023'))
    print(is_real_date('29.02.2020'))
    print(is_real_date('29.02.2021'))