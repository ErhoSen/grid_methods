import numpy as np

np.set_printoptions(precision=4, suppress=True)


def diag_domination(A, b):
    bigA = np.append(A, b, axis=1)
    print("\nИсходная матрица:\n", bigA)
    bigA[2] += bigA[1]*(-1)
    bigA[0] += bigA[1]*(-2)
    bigA[0], bigA[1] = bigA.copy()[1], bigA.copy()[0]
    bigA[0] += bigA[1] + bigA[2]
    print("\nДиагональное преобладание:\n", bigA)
    # return bigA
    return bigA[:, :3], bigA[:, 3]


def norm(arr):
    sum_of_squares = 0.0
    for elen in arr:
        sum_of_squares += elen**2
    return np.sqrt(sum_of_squares)


def s_iteration(C, d):
    eps = 0.000001
    num_of_iter = 0
    n = len(C)
    Xprev = np.array([0,0,0])  # Вектор значений неизвестных на предыдущей итерации

    while True:
        Xcurrent = [0,0,0]  # Вектор значений неизвестных на текущем шаге
        for i in range(n):  # [0,1,2]
            Xcurrent[i] = d[i]  # Иницируем свободным членом

            for j in range(n):  # [0,1,2]
                if (i != j):  # Вычитаем сумму по всем отличным от i-ой неизвестным
                    Xcurrent[i] -= C[i][j] * Xprev[j]

            Xcurrent[i] /= C[i][i]  # Делим на коэффицент при i-ой неизвестной

        if np.linalg.norm(np.array(Xprev) - np.array(Xcurrent)) < eps:  # Считаем погрешность
            break  # Если необходимая точность достигнута, завершаем процесс
        Xprev = Xcurrent
        num_of_iter += 1
    print("\n Колличество итераций:", num_of_iter)

    return Xcurrent


def main():
    A = np.array([
        [9.1, 5.6, 7.8],
        [3.8, 5.1, 2.8],
        [4.1, 5.7, 1.2],
    ])
    b = np.array([
        [9.8],
        [6.7],
        [5.8]
    ])
    C, d = diag_domination(A, b)
    result = s_iteration(C, d)
    print("\nResult:\n", result)

if __name__ == '__main__':
    main()

# [-0.3704  1.0938  0.9032]