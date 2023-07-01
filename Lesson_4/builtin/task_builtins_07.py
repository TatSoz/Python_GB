"""all(iterable"""


def all_(iterable):
    for element in iterable:
        if not element:
            return False
    return True


numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('Все элементы отрицательные и/или нулевые')

if all_(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('Все элементы отрицательные и/или нулевые')