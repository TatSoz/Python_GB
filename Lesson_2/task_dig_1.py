# x = int('42')
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, sep='\n')


import  sys
STEP = 2 ** 16
num = 1
for _ in range(30):         # знак _ указывает что переменная не нужна
    print(sys.getsizeof(num), num)
    num *= STEP


