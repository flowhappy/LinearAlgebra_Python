from py_LA.LinerSystem import LinerSystem
from py_LA.Vector import Vector
from py_LA.Matrix import Matrix

if __name__ == '__main__':
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinerSystem(A,b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
