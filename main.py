import math
import numpy as np
import random as rnd

def task1():
    A = np.random.randint(0, 9, (6, 6))
    B = np.array([A[4, :], A[5, :]])
    C = np.transpose(np.array([A[:, 0], A[:, 1]]))
    print("Исходная матрица\n", A)
    print("\nМатрица из двух последних строк исходной матрицы 2x6\n", B)
    print("\nМатрица из двух первых столбцов исходной матрицы 6x2\n", C)

def task2():
    A = np.random.randint(0, 9, (6, 6))
    B = np.array([A[4, :], A[5, :]])
    C = np.transpose(np.array([A[:, 0], A[:, 1]]))
    D = np.zeros((2, 2), dtype=int)


    for i in range(2):
        for j in range(2):
            D[i, j] = np.dot(B[i, :], C[:, j])


    print("Векторное перемножение матриц\n", D)

    print("Библиотечное перемножение матриц\n", np.dot(B, C))




def task3():
    def norm3(A):
        norm = 0
        for i in range(10):
            norm += abs(A[0][i])**3
        norm = norm**(1/3)
        return norm
    A = np.random.randint(-100, 100, (1, 10))

    print(A)
    print("Норма вектора(самописная): ", norm3(A), "\n")
    print("Норма вектора(бибилиотечная): ", np.linalg.norm(A, ord=3, axis=1))

def task4():
    def norminf(A):
        sum = 0
        norm = 0
        for i in range(10):
            for j in range(10):
                sum += abs(A[i][j])
            norm = max(norm, sum)
            sum = 0
        return norm

    A = np.random.randint(-100, 100, (10, 10))

    print(A)
    print(A[0][1])
    print("Норма вектора(библиотечная): ", np.linalg.norm(A, ord=np.inf), "\n")
    print("Норма вектора(самописная):", norminf(A))

def task5():
    A = np.random.randint(-100, 100, (1, 10))
    print(A)

    b = np.sign(-A[0]) * np.linalg.norm(A)
    u = A.copy()
    u[0] -= b
    v = u / np.linalg.norm(u)

    HH = np.eye(8) - 2.0 * np.outer(v, np.transpose(v))
    print(np.dot(HH, A))
    print(np.linalg.norm(A), np.linalg.norm(np.dot(HH, A)))













if __name__ == '__main__':
    task5()

