from py_LA.LU import lu
from py_LA.Matrix import Matrix

if __name__ == '__main__':
    A = Matrix([[1, 2, 3], [4, 5, 6], [3, -3, 5]])
    L, U = lu(A)
    print(L)
    print(U)
