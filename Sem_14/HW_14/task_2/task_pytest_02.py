import pytest


def test_simple_number():
    assert 'Число является простым' == check_number(5)

def test_composite_number():
    assert 'Число является составным' == check_number(4)

def test_wrong_number():
    assert 'Введённое число не входит в заданный диапазон' == check_number(-3)

def test_one_number():
    assert 'Число 1 не является ни простым, ни составным' == check_number(1)



def check_number(num: int):

    MIN = 0
    MAX = 100000

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
    pytest.main(['-vv'])