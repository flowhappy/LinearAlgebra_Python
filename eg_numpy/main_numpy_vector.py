import numpy as np

if __name__ == '__main__':
    # 使用numpy创建数组
    vec1 = np.array([1, 2, 3])
    print(vec1)
    # [1 2 3]

    # 使用numpy创建零向量, 浮点类型
    vec0 = np.zeros(5)
    print(vec0)
    # [0. 0. 0. 0. 0.]

    # 使用numpy创建纬度为5，值为1和其他值的向量
    vec2 = np.ones(5)
    vec3 = np.full(5, 666)
    print(vec2, vec3)
    # [1. 1. 1. 1. 1.] [666 666 666 666 666]

    # 获得向量的元素的数量
    print(vec1.size)
    # 3

    # 索引，切片
    print(vec1[0], vec1[-1], vec2[1:3])
    # 1 3 [1. 1.]

    # 加减乘除基本运算参考Vector.py
    # 点乘
    print(vec1.dot(np.array([4, 5, 6])))
    # 32

    # 向量的模
    print(np.linalg.norm(vec1))
    # 3.7416573867739413
