# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


def format_str(text: str) -> None:
    formatted_text = sorted(text.split())

    # max_word = ''
    # for item in formatted_text:
    #     if len(max_word) < len(item):
    #         max_word = item

    max_word = len(max(formatted_text, key=len))
    for index, item in enumerate(formatted_text, 1):
        print(f'{index}. {item:>{max_word}}')

if __name__ == '__main__':
    st = input('Введите строку: ')
    format_str(st)




