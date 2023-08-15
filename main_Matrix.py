from py_LA.Matrix import Matrix
from py_LA.Vector import Vector

if __name__ == '__main__':
    mar = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(mar.shape())
    print(mar.row_num(), mar.col_num())
    print(mar.size())
    print(mar[0, 1])
    print(mar.row_vector(0))
    mar2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    print(mar + mar2)
    print(mar - mar2)
    print(mar * 2)
    print(2 * mar)
    print(mar / 2)

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(T.dot_mul(p))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print(T.dot_mul(P))

    print(mar)
    print(mar.T())
