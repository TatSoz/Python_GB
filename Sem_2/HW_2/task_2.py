# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

SYSTEM = 16
def dec_to_hex(input_number):
    result = ""

    list_result = []
    remains = None
    divisible = None
    list_result.append(str(input_number % SYSTEM))
    remains = input_number % SYSTEM
    divisible = input_number // SYSTEM

    while divisible != 0:
        remains = divisible % SYSTEM
        divisible //= SYSTEM
        list_result.append(str(remains))

    list_result.reverse()

    for i in list_result:
        if i == "10":
            result += "a"
        elif i == "11":
            result += "b"
        elif i == "12":
            result += "c"
        elif i == "13":
            result += "d"
        elif i == "14":
            result += "e"
        elif i == "15":
            result += "f"
        else:
            result += i
    return result



if __name__ == '__main__':
    user_input = int(input('Введите  целое положительное число: '))

    print(f'Это число в шестнадцатеричном представлении - {dec_to_hex(user_input)}')
    print(f'Проверка результата с помощью встроенной функцией hex - {hex(user_input)}')







