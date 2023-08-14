from py_LA.Matrix import Matrix

if __name__ == '__main__':
    mar = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(mar.shape())
    print(mar.row_num(), mar.col_num())
    print(mar.size())
    print(mar[0, 1])
    print(mar.row_vector(0))
