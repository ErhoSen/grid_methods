import numpy as np

np.set_printoptions(precision=4, suppress=True)

def like_a_boss(bigA):
    multiplier1 = -bigA[1][0]/bigA[0][0]
    multiplier2 = -bigA[2][0]/bigA[0][0]
    bigA[1] += bigA[0]*multiplier1
    bigA[2] += bigA[0]*multiplier2
    print(bigA)

    multiplier = -bigA[2][1]/bigA[1][1]
    bigA[2] += bigA[1]*multiplier
    print(bigA)

    # Revers
    multiplier1 = -bigA[1][2]/bigA[2][2]
    multiplier2 = -bigA[0][2]/bigA[2][2]
    bigA[1] += bigA[2]*multiplier1
    bigA[0] += bigA[2]*multiplier2
    print(bigA)

    multiplier = -bigA[0][1]/bigA[1][1]
    bigA[0] += bigA[1]*multiplier
    print(bigA)

    # Result
    bigA[0] /= bigA[0][0]
    bigA[1] /= bigA[1][1]
    bigA[2] /= bigA[2][2]
    result = bigA[:, 3]
    print(bigA)
    return result

def gaussian(bigA):
    n = len(bigA)  # 3

    print("Прямой ход:")
    for base_row in range(n-1):  # [0,1]
        for row in range(base_row+1, n):
            multiplier = -bigA[row][base_row]/bigA[base_row][base_row]
            bigA[row] += bigA[base_row]*multiplier
    print(bigA, end="\n\n")

    print("Обратный ход:")
    for base_row in range(n-1,0, -1):  # [2,1]
        for row in range(base_row-1, -1, -1):  # [1,0, [0]
            multiplier = -bigA[row][base_row]/bigA[base_row][base_row]
            bigA[row] += bigA[base_row]*multiplier
    print(bigA, end="\n\n"

    print("Результат:")
    for row in range(n):
        bigA[row] /= bigA[row][row]
    print(bigA, end="\n\n")
    result = bigA[:, n]
    return result

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
    bigA = np.append(A, b, axis=1)
    print("Исходная матрица:")
    print(bigA, end="\n\n")

    # result = like_a_boss(bigA.copy())
    result = gaussian(bigA.copy())
    print(result)

if __name__ == '__main__':
    main()