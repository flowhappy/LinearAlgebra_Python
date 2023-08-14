from py_LA.Vector import Vector


class Matrix:
    def __init__(self, list2d):
        # 将二维数组的每一行取出来，再复制
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return "Matrix({})".format(self._values)

    # 让两个方法相等
    __str__ = __repr__

    def shape(self):
        """
        :return: 矩阵有几行几列，前者返回行数，后者返回第一行的元素个数，就是列数
        """
        return len(self._values), len(self._values[0])

    def row_num(self):
        """
        :return: 返回矩阵的行数
        """
        return self.shape()[0]

    def col_num(self):
        """
        :return: 返回矩阵的列数
        """
        return self.shape()[1]

    def size(self):
        """
        :return: 返回矩阵的元素个数
        """
        return self.col_num() * self.row_num()

    def __getitem__(self, item):
        # 获得某一个元素
        return self._values[item[0]][item[1]]

    def row_vector(self, index):
        # 返回第几行的元素
        return Vector(self._values[index])

    def col_vector(self, index):
        # 返回第index列的元素
        return Vector(row[index] for row in self._values)
