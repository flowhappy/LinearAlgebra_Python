from py_LA.Determinant import Determinant

det1 = Determinant([[1, 4, -1, 4], [2, 2, 2, 3], [3, -1, 6, 2], [4, 0, 5, 3]])
det2 = Determinant([[0, 5, 2, 0], [8, 3, 5, 4], [7, 2, 4, 1], [0, 4, 1, 0]])
det3 = Determinant([[2, 2, 2], [2, 2, 2], [3, 3, 3]])

print(det1.result())
