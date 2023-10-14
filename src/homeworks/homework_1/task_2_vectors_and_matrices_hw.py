import math


def scalar_product(x, y):
    return sum(i*j for (i, j) in zip(x, y))


def length(x):
    return sum(i*j for (i, j) in zip(x, x)) ** 0.5


def angle(x, y):
    return ((math.acos(scalar_product(x, y) / (length(x) * length(y)))) * 180) / math.pi


def print_matrix(matrix):
    matrix1 = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix1 += str(matrix[i][j])
            matrix1 += " "
        matrix1 += "\n"
    print(matrix1)


def transposition(matrix_):
    return [[matrix_[l][k] for l in range(len(matrix_))]for k in range(len(matrix_[0]))]


def matrix_sum(matrix_1, matrix_2):
    return [[matrix_1[k][l] + matrix_2[k][l] for l in range(len(matrix_1[0]))] for k in range(len(matrix_1))]


def matrix_product(matrix_1, matrix_2):
    matrix_2 = transposition(matrix_2)
    return transposition([[scalar_product(matrix_1[i], matrix_2[j]) for i in range(len(matrix_1))] for j in range(len(matrix_2))])


def case_vector():
    print("Выберите операцию с векторами:")
    print("Нажмите 1 чтобы посчитать скалярное произведение")
    print("Нажмите 2 чтобы посчитать длинну вектора")
    print("Нажмите 3 чтобы посчитать угол между векторами")

    operator = int(input())

    x1 = [int(num) for num in input("Введите вектор: ").split()]

    if operator != 2:
        x2 = [int(num) for num in input("Введите вектор: ").split()]

    if operator == 1:
        print(scalar_product(x1, x2))
    elif operator == 2:
        print(length(x1))
    elif operator == 3:
        print(angle(x1, x2), "°", sep="")


def case_matrix():
    print("Выберите операцию с матрицами:")
    print("Нажмите 1 чтобы транспонировать матрицу")
    print("Нажмите 2 чтобы сложить матрицы")
    print("Нажмите 3 чтобы перемножить матрицы")

    operator = int(input())

    if operator == 1:
        n = int(input("Введите количество строк матрицы:"))
        print("Введите матрицу по строкам:")
        matrix = [list(map(int, input().split())) for i in range(n)]
        print_matrix(transposition(matrix))

    elif operator == 2:
        n = int(input("Введите количество строк матриц:"))
        print("Введите первую матрицу по строкам:")
        matrix1_ = [list(map(int, input().split())) for i in range(n)]

        print("Введите вторую матрицу по строкам:")
        matrix2_ = [list(map(int, input().split())) for i in range(n)]

        print_matrix(matrix_sum(matrix1_, matrix2_))

    elif operator == 3:
        n = int(input("Введите количество строк матрицы:"))
        print("Введите первую матрицу по строкам:")
        matrix1_ = [list(map(int, input().split())) for i in range(n)]

        print("Введите вторую матрицу по строкам:")
        matrix2_ = [list(map(int, input().split())) for i in range(len(matrix1_[0]))]

        print_matrix(matrix_product(matrix1_, matrix2_))



if __name__ == '__main__':
    print("С чем будем работать?")
    print("Нажмите 1 чтобы продолжить работу с векторами")
    print("Нажмите 2 чтобы продолжить работу с матрицами")

    option = int(input())
    if option == 1:
        case_vector()

    elif option == 2:
        case_matrix()