# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры.

import os.path
import pytest
import json
from task_project import Project
from task_user import UserData
from task_excet import MyAccessEx



JSON_FILE = 'task_6.json'

@pytest.fixture
def users():
    data = {
        UserData('John', 11, 2),
        UserData('Vasya', 12, 3),
        UserData('Peter', 13, 6),
        }
    return data

@pytest.fixture
def level_current_user():
    return UserData('John', 11, 2)

@pytest.fixture
def new_current_user():
    return UserData('Kolya', 8, 1)



def test_load_json(users):
    data = {
        2: {11: 'John'},
        3: {12: 'Vasya'},
        6: {13: 'Peter'}
    }
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=True)
    p1 = Project()
    test_result = p1.load_json(JSON_FILE)
    assert test_result == users

def test_add_user(new_current_user):
    """Тестирование добавление пользователя"""
    test_project = Project()
    test_project.load_json(JSON_FILE)
    test_project.enter('John', 11)
    user_to_add = test_project.add_user('Kolya', 8, 3)
    assert user_to_add == new_current_user



def test_enter_valid_user(level_current_user):
    """Тестирование входа в систему существующего пользователя"""
    new_pr = Project()
    new_pr.load_json(JSON_FILE)
    test_user = new_pr.enter('John', 11)
    assert test_user == level_current_user


def test_enter_new_user():
    """ Тестирование входа в систему  пользователя, который отсутствует в списке"""
    with pytest.raises(MyAccessEx):
        test_project = Project()
        test_project.load_json(JSON_FILE)
        test_dict = test_project.enter('Jim', 15)
        assert users != test_dict


if __name__ == '__main__':
    pytest.main(['-vv'])













