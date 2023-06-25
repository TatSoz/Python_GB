num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)

print((0.1 + 0.2))         # 0.300000000004
pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375            # 3.141592653589793
print(pi)


DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по уполмочанию: '))
level = num or DEFAULT
print(level)

name = input('ак вас зовут? ')
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, приветствую')


data = [0, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())

    



