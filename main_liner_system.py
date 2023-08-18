from py_LA.LinerSystem import LinerSystem
from py_LA.Vector import Vector
from py_LA.Matrix import Matrix

if __name__ == '__main__':
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinerSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()

    print()
    A2 = Matrix([[2, 2], [2, 1], [1, 2]])
    b2 = Vector([3, 2.5, 7])
    ls2 = LinerSystem(A2, b2)
    if not ls2.gauss_jordan_elimination():
        print("no solution!")
    ls2.fancy_print()
