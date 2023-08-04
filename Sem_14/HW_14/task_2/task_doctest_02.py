MIN = 0
MAX = 100000

def check_number(num: int):
    """
    >>> check_number(5)
    'Число является простым'
    >>> check_number(4)
    'Число является составным'
    >>> check_number(-3)
    'Введённое число не входит в заданный диапазон'
    >>> check_number(1)
    'Число 1 не является ни простым, ни составным'
    """

    if num == 1:
        return 'Число 1 не является ни простым, ни составным'
    elif MIN < num < MAX:
        count = 0
        for i in range(2, num):
            if (num % i == 0):
                count += 1
        if (count <= 0):
            return 'Число является простым'
        else:
            return 'Число является составным'
    else:
        return 'Введённое число не входит в заданный диапазон'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

