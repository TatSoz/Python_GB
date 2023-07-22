# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from task_3 import Person
class Employee(Person):
    MAX_LEVEL = 7
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id: int):
        super().__init__(last_name, first_name, patronymic, age)
        if 100_000 <= id <= 999_999:
            self.id = id
        else:
            self.id = 100_000

    def get_level(self):
        z = sum(int(num) for num in str(self.id))
        return z % self.MAX_LEVEL


if __name__ == '__main__':
    emp = Employee('Семенов', 'Семен', 'Семенович', 18, 834_456)
    print(emp.get_level())



