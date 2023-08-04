# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры.
import os.path
import pytest
import json
from task_project import Project
from task_user import UserData, data_from_json



JSON_FILE = 'task_6.json'

@pytest.fixture
def setup():
    data = {
        UserData('John', 11, 1),
        UserData('Vasya', 12, 3),
        UserData('Peter', 13, 6),
        }
    return data


# def test_write_json():
#     with open(JSON_FILE, 'w', encoding='utf-8') as j:
#         json.dump(setup, j)
#     assert os.path.exists(JSON_FILE)


def test_load_json(setup):
    # test_result = data_from_json(JSON_FILE)
    p1 = Project()
    test_result = p1.load_json(JSON_FILE)
    assert setup == test_result

def test_add_user():
    test_project = Project()
    test_project.load_json(JSON_FILE)
    test_dict = test_project.enter('Kolya', 14)
    assert setup == test_dict


def test_not_add_user():
    test_project = Project()
    test_project.load_json(JSON_FILE)
    test_dict = test_project.enter('Kolya', 11)
    assert setup != test_dict


if __name__ == '__main__':
    pytest.main(['-v'])













