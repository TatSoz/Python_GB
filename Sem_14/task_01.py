# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

# def del_symbols(text: str) -> str:
#     text_new = ''
#     for sym in text:
#         if sym in set(ascii_letters + ' '):
#             text_new += sym
#     return text_new.lower()

def del_symbols(text: str) -> str:
    text_new = ''.join(sym for sym in text if sym in set(ascii_letters + ' '))
    return text_new.lower()


if __name__ == '__main__':
    new_txt = 'Hello world!, Я изучаю Питон.'
    print(del_symbols(new_txt))