class Determinant:

    """
    1. 取负 函数
    2. 交换两行 函数
    3. 行相加 函数
    """
    def __init__(self, matrix):
        assert len(matrix) == len(matrix[0]), "must be a square"
        self._values = matrix
        self._row_num = len(matrix)

    def triangle_up(self):
        row_num = len(self._values)
        for i in range(row_num - 1):
            for j in range(i + 1, row_num):
                k = self._values[j][i] / self._values[i][i]
                for l in range(row_num):
                    self._values[j][l] = self._values[j][l] - self._values[i][l] * k

    def result(self):
        res = 1
        self.triangle_up()
        for i in range(self._row_num):
            res = res * self._values[i][i]
        return res
