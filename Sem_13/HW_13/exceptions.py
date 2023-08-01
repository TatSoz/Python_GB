class BasicException(Exception):
    pass


class SizeError(BasicException):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == 'сложение или вычетание':
            return 'Матрицы должны быть одинакового размера!'
        elif self.operation == 'умножение':
            return 'Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!'
        else:
            return 'Невозможно сравнить. Матрицы разных размеров'



class UserTypeStrError(BasicException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение {self.value} должно быть текстом'


class UserTypeTextError(BasicException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isalpha():
            return f'Значение {self.value} должно содержать только буквы'
        elif not self.value.istitle():
            return f'Значение {self.value} должно начинаться с заглавной буквы'


class UserLessonsError(BasicException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'"Предмет {self.value} не изучается данным студентом"'


class UserEstimateError(BasicException):
    def __init__(self, value, lower, upper):
        self.value = value
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = ''
        if self.value < self.lower:
            text = 'меньше нижней'
        elif self.value > self.lower:
            text = 'больше верхней'
        return f'Оценка {self.value} {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'