# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

from exceptions import SizeError
class Matrix:
    """Класс матрица. Производит базовые действия сложение, вычитание, умножение матриц, сравнение."""

    def __init__(self, rows: int = 2, cols: int = 2, init_value: int = 0, *, matrix: list[list[int]] = None):
        """Инициализация матрицы по умолчанию 2 строки и 2 колонки

        :rows: Количество строк.
        :cols: Количество колонок.
        :init_value: Значение для инициализации матрицы.
        :matrix: Готовая матрица.
        """

        if matrix is None:
            self.__matrix = []
            for _ in range(rows):
                self.__matrix.append([init_value for _ in range(cols)])
        else:
            rows = len(matrix)
            cols = len(matrix[0])
            self.__matrix = matrix

        self.__cols = cols
        self.__rows = rows

    def __add__(self, other):
        """Сложение матриц"""

        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise SizeError('сложение или вычетание')
            # return 'Матрицы должны быть одинакового размера!'

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]

        return result

    def __sub__(self, other):
        """Вычитание матриц"""

        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise SizeError('сложение или вычетание')
            # return 'Матрицы должны быть одинакового размера'

        result = Matrix(self.__rows, self.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] - other.__matrix[i][j]

        return result

    def __str__(self):
        """Вывод матрицы на печать."""

        result = []
        for row in self.__matrix:
            for val in row:
                result.append(f'{val:2}\t')
            result.append('\n')
        return ''.join(result)

    def __repr__(self):
        """Отображение матрицы."""

        return f'Matrix(matrix={self.__matrix})'

    def __eq__(self, other):
        """Сравнение матриц."""

        result = True
        if self.__rows != other.__rows or self.__cols != other.__cols:
            raise SizeError('eq')
        else:
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if self.__matrix[i][j] != other.__matrix[i][j]:
                        result = False
                        break
                if not result:
                    break

        return result

    def __mul__(self, other):
        """Умножение матриц."""


        if self.__cols != other.__rows:
            raise SizeError('умножение')
            # return 'Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!'

        result = Matrix(self.__rows, other.__cols)
        for i in range(result.__rows):
            for j in range(result.__cols):
                for k in range(result.__cols):
                    result.__matrix[i][j] = self.__matrix[i][k] * other.__matrix[j][k]

        return result


if __name__ == '__main__':
    matrix_1 = Matrix(matrix=[[2, 3, 8], [4, 6, 9], [1, 3, 6]])
    matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
    # matrix_2 = Matrix(matrix=[[4, 2, 8], [7, 1, 5]])

    print('Матрица 1')
    print(matrix_1)
    print('Матрица 2')
    print(matrix_2)
    print(f'{matrix_1 = }')
    print(f'{matrix_2 = }')

    matrix_add = matrix_1 + matrix_2
    matrix_sub = matrix_1 - matrix_2

    print('Сложение matrix_1 + matrix_2')
    print(matrix_add)
    print('Вычитание matrix_1 - matrix_2')
    print(matrix_sub)

    print(f'Сравнение matrix_1 == matrix_1 - {matrix_1 == matrix_1}')
    print(f'Сравнение matrix_1 == matrix_2 - {matrix_1 == matrix_2}')

    matrix_3 = Matrix(matrix=[[4, 2, 8], [7, 1, 5], [2, 8, 3]])
    matrix_4 = Matrix(matrix=[[4, 8], [1, 5]])

    print('Матрица 3')
    print(matrix_3)
    print('Матрица 4')
    print(matrix_4)

    print('matrix_1 * matrix_3')
    print(matrix_1 * matrix_3)
    print('matrix_1 * matrix_4')
    print(matrix_1 * matrix_4)
