# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.

def inp_numbers():
    while True:
        try:
            num = input('Введите число: ')
            num = int(num)
            print('Это целое число')
            break
        except ValueError:
            try:
                num = int(num)
                print(f'Это вещественное число')
                break
            except ValueError:
                print(f'Значение должно быть целым или вещественным числом!')
    return num


if __name__ == '__main__':
    inp_numbers()

