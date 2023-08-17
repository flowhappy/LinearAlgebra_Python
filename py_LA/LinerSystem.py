from Matrix import Matrix
from Vector import Vector


class LinerSystem:
    def __init__(self, A, b):
        """
        A: 系数矩阵
        b: 结果向量
        """
        assert A.row_num == len(b), "row number of A must be equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        assert self._m == self._n, "row_num must be equal to col_num"  # TODO: no this restriction
        """
        下面是实现增广矩阵的代码
            增广矩阵就是 系数矩阵+结果列向量
            使用向量类的underlying_list方法返回该向量的原数据（数据类型是列表）
            再直接使用➕来链接结果列向量
            这样实现一行的增广矩阵
            再通过遍历来获得完整的增广矩阵
        """
        self.Ab = [Vector(
            A.row_vector(i).underlying_list + b[i]
        ) for i in range(self._m)]

    def _max_row(self, index, n):
        """
        从第i行到第n行
        """
        best, ret = self.Ab[index][index], index
        """
        这里的self.Ab[i][index]就是取固定这一列，i进行行的递增变化
        为什么不直接使用[i][0]呢？
        因为不仅仅是第一次（第一行）需要选择最大行，往后确定每一行的主元的时候都要确定
        """
        for i in range(index + 1, n):
            if self.Ab[i][index] > best:
                # 此时，i是最大元素所在的行下标
                best, ret = self.Ab[i][index], i
        return ret

    def _forward(self):
        n = self._m
        for i in range(n):
            """
            Ab[i][i]为主元
            为了避免[0][0]元素是零，所以直接选择第一列元素最大的这一行，和第一行交换
            """
            max_row = self._max_row(i, n)
            # 交换
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]
            # 将这一行的主元化为1，就是这一行除以主元的值
            self.Ab[i] = self.Ab[i] / self.Ab[i][i]  # todo: ab[i][i] == 0
            # 至此已经确定主元，现在将主元所在行以下的所有行的主元所在列的元素化为0
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def _backward(self):
        n = self._m
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[i] * self.Ab[j][i]

    def gauss_jordan_elimination(self):
        self._forward()
        self._backward()

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|{}".format(self.Ab[i][-1]))
