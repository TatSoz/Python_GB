# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest
from string import ascii_letters


def test_without_changes():
    assert 'hello world' == del_symbols('hello world')


def test_change_register():
    assert 'hello world' == del_symbols('Hello world')


def test_del_symbols():
    assert 'hello' == del_symbols('hello!')


def test_del_other_lang():
    assert 'good morning ' == del_symbols('good morning студенты')


def test_all_cases():
    assert 'hello world   ' == del_symbols('Hello world! я изучаю Питон')



def del_symbols(text: str) -> str:
    text_new = ''.join(sym for sym in text if sym in set(ascii_letters + ' '))
    return text_new.lower()



if __name__ == '__main__':
    pytest.main(['-vv'])
