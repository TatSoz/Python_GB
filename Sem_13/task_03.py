# Создайте класс с базовым исключением и дочерние классы - исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyExClass(Exception):
    pass


class MyLevelEx(MyExClass):
    def __init__(self, level):
        if level < 8:
            self.level = 'low'


    def __str__(self):
        return f'Уровень доступа {self.level} слишком низок для доступа!'


class MyAccessEx(MyExClass):
    def __init__(self, acs):
        self.acs = acs

    def __str__(self):
        return f'Доступ запрещен!'


if __name__ == '__main__':
    lvl1= 5
    lvl2 = 9

    if lvl2 > 6:
        print('OK')
    else:
        raise MyLevelEx(lvl2)





