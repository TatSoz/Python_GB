LIMIT = 1000


def func(x, y):
    result = x ** y % LIMIT  # с константой работать в функциях допустимо
    return result


print(func(42, 73))