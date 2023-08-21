from py_LA.LinerSystem import rank
from py_LA.Vector import Vector
from py_LA.Matrix import Matrix


def gram_schmidt_process(basis):
    # 用矩阵的秩判断线性无关
    matrix = Matrix(basis)
    assert rank(matrix) == len(basis)
    res = [basis[0]]
    for i in range(1, len(basis)):
        p = basis[i]
        for r in res:
            p = p - basis[i].dot(r) / r.dot(r) * r
        res.append(p)
    return res
