def func(y: int) -> int:
    """"Глобальные переменные"""
    global x
    x += 100
    print(f'In function {x = }')
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')