from random import randint

# __all__ = ['func', '_secret']  # показывает, какие объекты импортировать при импорте со *

SIZE = 100
_secret = 'qwerty'  # защищённая переменная
__top_secret = 'dfgdfdfddf'  # приватная переменная


def func(a: int, b: int) -> str:
    z = f'От {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)
