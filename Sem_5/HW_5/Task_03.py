#  Создайте функцию генератор чисел Фибоначчи

def fib_gen(num):
    a, b = 0, 1
    for _ in range(num + 1):
        yield a
        a, b = b, a + b

n = int(input('Введите число: '))
for i in fib_gen(n):
    print(i, end=' ')

