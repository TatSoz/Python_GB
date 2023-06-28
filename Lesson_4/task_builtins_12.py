"""globals()"""

SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


print(globals())
print(f'{func(1, 2, 3) = }')


x = 42
global_dict = globals()
global_dict['x'] = 73
print(f'{x = }')