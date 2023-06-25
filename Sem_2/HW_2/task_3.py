# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму  и *произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def gcd(n, d):
    while d != 0:
        n, d = d, n % d
    return n


def check_eq(num, denom):
    gcd_num = gcd(num, denom)
    if num % denom == 0:
        return num // gcd_num
    return f'{num // gcd_num}/{denom // gcd_num}'


def add_frac(a, b, d_a, d_b):
    new_num_a, new_denom_a = a * d_b, d_a * d_b
    new_num_b, new_denom_b = b * d_a, d_b * d_a
    sum_num = new_num_a + new_num_b
    return check_eq(sum_num, new_denom_b)


def mult_frac(a, b, d_a, d_b):
    num = a * b
    denom = d_a * d_b
    return check_eq(num, denom)


if __name__ == '__main__':
    num_a, denom_a = map(int, input('Введите первую дробь вида a/b: ').split('/'))
    num_b, denom_b = map(int, input('Введите вторую дробь вида a/b: ').split('/'))

    print(f'Сложение дробей: {add_frac(num_a, num_b, denom_a, denom_b)}')
    print(f'Проверка сложения дробей: {Fraction(num_a, denom_a) + Fraction(num_b, denom_b)}')

    print(f'Произведение дробей: {mult_frac(num_a, num_b, denom_a, denom_b)}')
    print(f'Проверка произведения дробей: {Fraction(num_a, denom_a) * Fraction(num_b, denom_b)}')