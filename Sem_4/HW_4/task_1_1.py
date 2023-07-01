# Напишите функцию для транспонирования матрицы


def matrix_transposition(matr: list) -> list:
    trans_matrix = [*zip(*matr)]
    return trans_matrix

def print_matrix(matr: list) -> None:
    for row in matr:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    matrix = [[2, 4, 6, 8],
              [1, 3, 5, 7]]
    print('Исходная матрица: ')
    print_matrix(matrix)
    print('Транспонированная матрица: ')
    print_matrix(matrix_transposition(matrix))
