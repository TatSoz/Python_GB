from exceptions import UserTypeStrError, UserTypeTextError, UserEstimateError, UserLessonsError

class CheckName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что имя состоит только из букв и начинается на заглавную"""
        if not isinstance(value, str):
            raise UserTypeStrError(value)
        if not value.isalpha() or not value.istitle():
            raise UserTypeTextError(value)


class CheckSubject:
    def __init__(self, path):
        self.path = path

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что предмет находится в списке"""
        with open(self.path, 'r', newline='', encoding='utf-8') as c:
            if value.lower() not in [sub.strip() for sub in c]:
                raise UserLessonsError(value)


class CheckSubjectScore:
    def __init__(self, min_sub_score, max_sub_score):
        self.min_sub_score = min_sub_score
        self.max_sub_score = max_sub_score

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что оценки входят в диапазон"""
        if self.min_sub_score > value or value > self.max_sub_score:
            raise UserEstimateError(value, self.min_sub_score, self.max_sub_score)


class CheckTesttScore:
    def __init__(self, min_test_score, max_test_score):
        self.min_test_score = min_test_score
        self.max_test_score = max_test_score

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что оценки входят в диапазон"""
        if self.min_test_score > value or value > self.max_test_score:
            raise UserEstimateError(value, self.min_test_score, self.max_test_score)