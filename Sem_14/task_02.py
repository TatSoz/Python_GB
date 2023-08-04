# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters

def del_symbols(text: str) -> str:
    """
    >>> del_symbols('hello world')
    'hello world'
    >>> del_symbols('Hello world')
    'hello world'
    >>> del_symbols('hello world!')
    'hello world'
    >>> del_symbols('hello world Я изучаю Питон')
    'hello world   '
    >>> del_symbols('Hello test! Я изучаю Питон')
    'hello test   '
    """
    text_new = ''.join(sym for sym in text if sym in set(ascii_letters + ' '))
    return text_new.lower()



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # doctest.testmod()


