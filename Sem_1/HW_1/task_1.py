# (Задание 6) Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря (1582  год)
# В коде должны быть один input и один print

GREGORIAN_START = 1582
FOUR_YEARS = 4
HUNDRED_YEARS = 100
FOUR_HUNDRED_YEARS =400

year = int(input('Введите год в формате гггг: '))
type_year = ''


if year <= GREGORIAN_START:
    type_year = 'Год обычный'
else:
    if year % FOUR_YEARS != 0:
        type_year = 'Год обычный'
    elif year % HUNDRED_YEARS == 0:
        if year % FOUR_HUNDRED_YEARS == 0:
            type_year = 'Год високосный'
    else:
        type_year = 'Год високосный'

print(type_year)


# вариант 2
# if year < GREGORIAN_START or year % FOUR_YEARS != 0 or year % HUNDRED_YEARS == 0 and year % FOUR_HUNDRED_YEARS != 0:
#     type_year = 'Обычный'
# else:
#     type_year = 'Високосный'
#
# print(type_year)