from statistics import mean

import descriptors as des


class Student:
    """Класс описывающий студента"""
    first_name = des.CheckName()
    last_name = des.CheckName()
    patronymic = des.CheckName()
    subject = des.CheckSubject('subjects.csv')
    subject_score = des.CheckSubjectScore(min_sub_score=2, max_sub_score=5)
    test_score = des.CheckTesttScore(min_test_score=0, max_test_score=100)
    subjects = []

    def __init__(self, first_name, last_name, patronymic, subject, subject_score, test_score):
        """
        Конструктор класса
        :param first_name: Имя студента
        :param last_name: Фамилия студента
        :param patronymic: Отчество студента
        :param subject: Предмет студента
        :param subject_score: Оценка по предмету
        :param test_score: Оценка теста по предмету
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def add_subject(self, subject, subject_score, test_score):
        """Метод добавления нового предмета студенту"""
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def _update_subjects(self):
        """Метод добавления предмета в список предметов"""
        self.subjects.append({
            'subject': self.subject,
            'subject_score': self.subject_score,
            'test_score': self.test_score,
        })

    def get_avg(self):
        """Метод, возвращающий информацию по среднему балу за оценки и тесты"""
        avg_sub_score = mean(score['subject_score'] for score in self.subjects)
        avg_test_score = mean(score['test_score'] for score in self.subjects)
        return f"""Предметы студента: {', '.join([sub['subject'].title() for sub in self.subjects])}
                   Средний бал по урокам: {avg_sub_score}
                   Средний бал по тестам: {avg_test_score}\n"""


if __name__ == '__main__':
    st_1 = Student('Иван', 'Иванов', 'Иванович', 'геометрия', 5, 87)
    print(f'Успеваемость студента {st_1.full_name}:')
    print(st_1.get_avg())
    st_1.add_subject('физика', 5, 78)
    st_1.add_subject('алгебра', 4, 66)
    print(st_1.get_avg())

    # st_1.add_subject('астрономия', 5, 82)

