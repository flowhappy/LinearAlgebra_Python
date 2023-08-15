import matplotlib.pyplot as plt
from py_LA.Matrix import Matrix
from py_LA.Vector import Vector
import math

if __name__ == '__main__':
    points = [
        [0, 0], [0, 5], [3, 5], [3, 4], [1, 4],
        [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]
    ]

    x = [points[i][0] for i in range(len(points))]
    y = [points[i][1] for i in range(len(points))]

    # 调整绘制窗口的大小
    plt.figure(figsize=(5, 5))
    # X轴从-10到10
    plt.xlim(-10, 10)
    # Y轴从-10到10
    plt.ylim(-10, 10)

    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)

    # T = Matrix([[2, 0], [0, 1.5]])
    # 沿X轴翻转 的变换矩阵
    # T = Matrix([[1, 0], [0, -1]])
    # 沿Y轴翻转 的变换矩阵
    # T = Matrix([[-1, 0], [0, 1]])
    # 关于原点对称 的变换矩阵
    # T = Matrix([[-1, 0], [0, -1]])
    # 沿X轴错切 的变换矩阵
    # T = Matrix([[1, 0.5], [0, 1]])
    # 沿Y轴错切 的变换矩阵
    # T = Matrix([[1, 0], [0.5, 1]])
    # 旋转
    theta = math.pi / 3
    T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    P2 = T.dot_mul(P.T())

    plt.plot(
        [P2.col_vector(i)[0] for i in range(P2.col_num())],
        [P2.col_vector(i)[1] for i in range(P2.col_num())],
    )

    plt.show()
