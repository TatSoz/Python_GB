# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def dec_to_hex(number):
    hex_number = 16
    hex_base = '0123456789abcdef'
    hex_result = ''
    while number:
        number, remainder = divmod(number, hex_number)
        hex_result = hex_base[remainder] + hex_result
    return hex_result


if __name__ == '__main__':
    user_input = int(input('Введите  целое положительное число: '))

    print(f'Это число в шестнадцатеричном представлении - {dec_to_hex(user_input)}')
    print(f'Проверка результата с помощью встроенной функцией hex - {hex(user_input)}')